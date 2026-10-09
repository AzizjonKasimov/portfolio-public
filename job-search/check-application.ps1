[CmdletBinding()]
param(
    [string]$Company,
    [string]$Role,
    [string]$Platform,
    [string]$PostingId,
    [string]$Url,
    [string]$CsvPath = (Join-Path $PSScriptRoot "applications.csv")
)

if (-not (Test-Path -LiteralPath $CsvPath)) {
    throw "Application tracker not found: $CsvPath"
}

if (-not ($Company -or $Role -or $Platform -or $PostingId -or $Url)) {
    Write-Host "Provide at least one search value: -Company, -Role, -Platform, -PostingId, or -Url."
    exit 2
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

$rows = Import-Csv -LiteralPath $CsvPath

$matches = $rows | Where-Object {
    if ($PostingId -and $_.platform_posting_id -eq $PostingId) {
        return (-not $Platform -or (Test-ContainsText $_.platform $Platform))
    }

    if ($PostingId) {
        return $false
    }

    if ($Url -and ($_.posting_url -eq $Url -or (Test-ContainsText $_.posting_url $Url))) {
        return (-not $Platform -or (Test-ContainsText $_.platform $Platform))
    }

    if ($Url) {
        return $false
    }

    if ($Platform -and (Test-ContainsText $_.platform $Platform)) {
        if (-not $Company -and -not $Role) {
            return $true
        }

        $companyMatches = (-not $Company -or (Test-ContainsText $_.company $Company))
        $roleMatches = (-not $Role -or (Test-ContainsText $_.role_title $Role))
        return ($companyMatches -and $roleMatches)
    }

    if ($Company -and (Test-ContainsText $_.company $Company)) {
        if (-not $Role -or (Test-ContainsText $_.role_title $Role)) {
            return $true
        }
    }

    if ($Role -and -not $Company -and -not $Platform) {
        if (Test-ContainsText $_.role_title $Role) {
            return $true
        }
    }

    return $false
}

if (-not $matches) {
    Write-Host "No matching applications found."
    exit 0
}

$matches |
    Sort-Object date_applied, date_materials_prepared, company |
    Select-Object status, date_applied, outcome_date, platform, platform_posting_id, company, role_title, fit_level, visa_risk, language_risk, last_audited, posting_url, packet_path |
    Format-Table -AutoSize
