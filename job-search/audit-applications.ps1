[CmdletBinding()]
param(
    [string]$Platform,
    [string]$Status,
    [string]$FitLevel,
    [ValidateSet("high", "medium", "low", "unknown", "flagged")]
    [string]$Risk,
    [switch]$Detailed,
    # Rows older than this many days count as waiting too long (applied) or not acted on (leads).
    [int]$StaleDays = 30,
    [string]$CsvPath = (Join-Path $PSScriptRoot "applications.csv")
)

if (-not (Test-Path -LiteralPath $CsvPath)) {
    throw "Application tracker not found: $CsvPath"
}

function Test-ContainsText {
    param(
        [AllowNull()][string]$Value,
        [AllowNull()][string]$Needle
    )

    if ([string]::IsNullOrWhiteSpace($Value) -or [string]::IsNullOrWhiteSpace($Needle)) {
        return $false
    }

    return $Value.IndexOf($Needle, [StringComparison]::OrdinalIgnoreCase) -ge 0
}

function Get-OverallRisk {
    param([object]$Row)

    $riskValues = @($Row.visa_risk, $Row.language_risk) |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_) }

    if ($riskValues -contains "high") {
        return "high"
    }

    if ($riskValues -contains "medium") {
        return "medium"
    }

    if (-not [string]::IsNullOrWhiteSpace($Row.screening_risks)) {
        return "flagged"
    }

    if ($riskValues.Count -eq 0 -or $riskValues -contains "unknown") {
        return "unknown"
    }

    return "low"
}

function Get-DateOrNull {
    param([AllowNull()][string]$Value)

    if ([string]::IsNullOrWhiteSpace($Value) -or $Value.Length -lt 10) {
        return $null
    }

    $parsed = [datetime]::MinValue
    if ([datetime]::TryParseExact($Value.Substring(0, 10), "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture, [Globalization.DateTimeStyles]::None, [ref]$parsed)) {
        return $parsed
    }

    return $null
}

function Show-GroupSummary {
    param(
        [object[]]$Rows,
        [string]$Property,
        [string]$Title
    )

    Write-Host ""
    Write-Host $Title
    $Rows |
        ForEach-Object {
            $value = $_.$Property
            if ([string]::IsNullOrWhiteSpace($value)) {
                $_ | Add-Member -NotePropertyName "__audit_bucket" -NotePropertyValue "(blank)" -Force
            } else {
                $_ | Add-Member -NotePropertyName "__audit_bucket" -NotePropertyValue $value -Force
            }
            $_
        } |
        Group-Object __audit_bucket |
        Sort-Object -Property Count, Name -Descending |
        Select-Object @{Name = $Property; Expression = { $_.Name } }, Count |
        Format-Table -AutoSize
}

$rows = @(Import-Csv -LiteralPath $CsvPath)

$filtered = @($rows | Where-Object {
    if ($Platform -and -not (Test-ContainsText $_.platform $Platform)) {
        return $false
    }

    if ($Status -and $_.status -ne $Status) {
        return $false
    }

    if ($FitLevel -and $_.fit_level -ne $FitLevel) {
        return $false
    }

    if ($Risk -and (Get-OverallRisk $_) -ne $Risk) {
        return $false
    }

    return $true
})

Write-Host "Applications in report: $($filtered.Count) of $($rows.Count)"

if ($filtered.Count -eq 0) {
    exit 0
}

Show-GroupSummary -Rows $filtered -Property "status" -Title "By status"
Show-GroupSummary -Rows $filtered -Property "platform" -Title "By platform"
Show-GroupSummary -Rows $filtered -Property "fit_level" -Title "By fit level"
Show-GroupSummary -Rows $filtered -Property "tailoring_level" -Title "By tailoring level"

Write-Host ""
Write-Host "By overall screening risk"
$filtered |
    ForEach-Object {
        [pscustomobject]@{
            risk = Get-OverallRisk $_
        }
    } |
    Group-Object risk |
    Sort-Object -Property Count, Name -Descending |
    Select-Object @{Name = "risk"; Expression = { $_.Name } }, Count |
    Format-Table -AutoSize

$needsAudit = @($filtered | Where-Object {
    ($_.status -in @("rejected", "withdrawn", "closed", "expired") -and [string]::IsNullOrWhiteSpace($_.last_audited)) -or
    ($_.status -eq "rejected" -and [string]::IsNullOrWhiteSpace($_.audit_summary))
})

$today = (Get-Date).Date

$waitingOnReply = @($filtered | Where-Object {
    if ($_.status -notin @("applied", "follow_up_needed")) {
        return $false
    }

    $applied = Get-DateOrNull $_.date_applied
    return $null -ne $applied -and ($today - $applied).Days -gt $StaleDays
})

$staleLeads = @($filtered | Where-Object {
    if ($_.status -notin @("found", "materials_prepared", "on_hold")) {
        return $false
    }

    $found = Get-DateOrNull $_.date_found
    return $null -ne $found -and ($today - $found).Days -gt $StaleDays
})

$missingFit = @($filtered | Where-Object {
    [string]::IsNullOrWhiteSpace($_.fit_level) -or
    [string]::IsNullOrWhiteSpace($_.selection_rationale) -or
    [string]::IsNullOrWhiteSpace($_.tailoring_level)
})

Write-Host ""
Write-Host "Needs outcome audit: $($needsAudit.Count)"
if ($needsAudit.Count -gt 0) {
    $needsAudit |
        Sort-Object outcome_date, date_applied, company |
        Select-Object status, outcome_date, platform, company, role_title, fit_level, audit_summary |
        Format-Table -AutoSize
}

Write-Host ""
Write-Host "Applied more than $StaleDays days ago with no outcome yet: $($waitingOnReply.Count)"
Write-Host "Leads found more than $StaleDays days ago and never submitted: $($staleLeads.Count)"
if ($Detailed) {
    if ($waitingOnReply.Count -gt 0) {
        Write-Host ""
        Write-Host "Waiting on a reply (oldest first)"
        $waitingOnReply |
            Sort-Object date_applied, company |
            Select-Object date_applied, platform, company, role_title, fit_level, next_follow_up |
            Format-Table -AutoSize
    }

    if ($staleLeads.Count -gt 0) {
        Write-Host ""
        Write-Host "Leads not acted on (oldest first)"
        $staleLeads |
            Sort-Object date_found, company |
            Select-Object date_found, status, platform, company, role_title, fit_level, deadline |
            Format-Table -AutoSize
    }
} elseif ($waitingOnReply.Count + $staleLeads.Count -gt 0) {
    Write-Host "Use -Detailed to list them."
}

Write-Host ""
Write-Host "Missing fit or tailoring fields: $($missingFit.Count)"
if ($missingFit.Count -gt 0) {
    $missingFit |
        Sort-Object status, platform, company |
        Select-Object status, platform, company, role_title, fit_level, tailoring_level, selection_rationale |
        Format-Table -AutoSize
}

if ($Detailed) {
    Write-Host ""
    Write-Host "Detailed rows"
    $filtered |
        Sort-Object status, platform, company |
        Select-Object status, date_applied, outcome_date, platform, company, role_title, fit_level, visa_risk, language_risk, tailoring_level, outcome_stage, audit_summary |
        Format-Table -AutoSize
}
