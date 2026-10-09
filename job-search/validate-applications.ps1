[CmdletBinding()]
param(
    [string]$CsvPath = (Join-Path $PSScriptRoot "applications.csv"),
    [string]$EventsPath = (Join-Path $PSScriptRoot "application-events.csv")
)

if (-not (Test-Path -LiteralPath $CsvPath)) {
    throw "Application tracker not found: $CsvPath"
}

$validStatuses = @(
    "found",
    "materials_prepared",
    "applied",
    "follow_up_needed",
    "interview",
    "offer",
    "rejected",
    "no_response",
    "withdrawn",
    "expired",
    "closed",
    "duplicate",
    "on_hold",
    "skipped"
)

$statusesThatMayHaveDateApplied = @(
    "applied",
    "follow_up_needed",
    "interview",
    "offer",
    "rejected",
    "no_response",
    "withdrawn",
    "closed"
)

$expectedApplicationColumns = @(
    "application_id",
    "company",
    "role_title",
    "role_family",
    "platform",
    "platform_posting_id",
    "posting_url",
    "location",
    "work_arrangement",
    "date_found",
    "deadline",
    "date_materials_prepared",
    "date_applied",
    "status",
    "application_method",
    "resume_path",
    "cover_letter_path",
    "packet_path",
    "details_path",
    "visa_signal",
    "language_signal",
    "fit_level",
    "fit_confidence",
    "selection_rationale",
    "screening_risks",
    "visa_risk",
    "language_risk",
    "tailoring_level",
    "profile_snapshot_path",
    "posting_snapshot_path",
    "next_follow_up",
    "outcome_date",
    "outcome_stage",
    "outcome_reason_reported",
    "duplicate_check_key",
    "last_audited",
    "audit_summary",
    "audit_confidence",
    "notes"
)

$validFitLevels = @(
    "strong",
    "good",
    "adjacent",
    "stretch",
    "unknown"
)

$validConfidenceValues = @(
    "low",
    "medium",
    "high",
    "unknown"
)

$validRiskValues = @(
    "low",
    "medium",
    "high",
    "unknown"
)

$validTailoringLevels = @(
    "generic",
    "profile_only",
    "role_family",
    "role_specific",
    "company_specific",
    "unknown"
)

$validOutcomeStages = @(
    "pre_screen",
    "recruiter_screen",
    "hiring_manager",
    "assessment",
    "interview",
    "offer",
    "post_offer",
    "unknown"
)

$validEventTypes = @(
    "found",
    "materials_prepared",
    "applied",
    "follow_up",
    "outcome_received",
    "audit",
    "note",
    "profile_updated",
    "posting_snapshot",
    "follow_up_needed",
    "skipped",
    "withdrawn",
    "closed"
)

$requiredFields = @(
    "application_id",
    "company",
    "role_title",
    "platform",
    "date_found",
    "status",
    "duplicate_check_key"
)

$rows = Import-Csv -LiteralPath $CsvPath
$errors = New-Object System.Collections.Generic.List[string]
$repoRoot = Split-Path -Parent $PSScriptRoot
$pathFields = @(
    "resume_path",
    "cover_letter_path",
    "packet_path",
    "details_path",
    "profile_snapshot_path",
    "posting_snapshot_path"
)

$eventRequiredFields = @(
    "event_id",
    "application_id",
    "event_date",
    "event_type",
    "status_after",
    "source",
    "event_summary",
    "created_at"
)

function Add-InvalidEnumError {
    param(
        [System.Collections.Generic.List[string]]$Errors,
        [int]$LineNumber,
        [object]$Row,
        [string]$Field,
        [string[]]$AllowedValues
    )

    $value = $Row.$Field
    if (-not [string]::IsNullOrWhiteSpace($value) -and $AllowedValues -notcontains $value) {
        $Errors.Add("Line ${LineNumber}: invalid $field '$value'. Allowed values: $($AllowedValues -join ', ').")
    }
}

for ($i = 0; $i -lt $rows.Count; $i++) {
    $row = $rows[$i]
    $lineNumber = $i + 2

    foreach ($field in $requiredFields) {
        if ([string]::IsNullOrWhiteSpace($row.$field)) {
            $errors.Add("Line ${lineNumber}: missing required field '$field'.")
        }
    }

    if ($row.status -and $validStatuses -notcontains $row.status) {
        $errors.Add("Line ${lineNumber}: invalid status '$($row.status)'.")
    }

    Add-InvalidEnumError -Errors $errors -LineNumber $lineNumber -Row $row -Field "fit_level" -AllowedValues $validFitLevels
    Add-InvalidEnumError -Errors $errors -LineNumber $lineNumber -Row $row -Field "fit_confidence" -AllowedValues $validConfidenceValues
    Add-InvalidEnumError -Errors $errors -LineNumber $lineNumber -Row $row -Field "visa_risk" -AllowedValues $validRiskValues
    Add-InvalidEnumError -Errors $errors -LineNumber $lineNumber -Row $row -Field "language_risk" -AllowedValues $validRiskValues
    Add-InvalidEnumError -Errors $errors -LineNumber $lineNumber -Row $row -Field "tailoring_level" -AllowedValues $validTailoringLevels
    Add-InvalidEnumError -Errors $errors -LineNumber $lineNumber -Row $row -Field "outcome_stage" -AllowedValues $validOutcomeStages
    Add-InvalidEnumError -Errors $errors -LineNumber $lineNumber -Row $row -Field "audit_confidence" -AllowedValues $validConfidenceValues

    if ($row.status -eq "applied" -and [string]::IsNullOrWhiteSpace($row.date_applied)) {
        $errors.Add("Line ${lineNumber}: status is applied but date_applied is empty.")
    }

    if ($row.status -eq "materials_prepared" -and [string]::IsNullOrWhiteSpace($row.date_materials_prepared)) {
        $errors.Add("Line ${lineNumber}: status is materials_prepared but date_materials_prepared is empty.")
    }

    if (-not [string]::IsNullOrWhiteSpace($row.date_applied) -and $statusesThatMayHaveDateApplied -notcontains $row.status) {
        $errors.Add("Line ${lineNumber}: date_applied is set but status is '$($row.status)'.")
    }

    foreach ($field in $pathFields) {
        $relativePath = $row.$field

        if (-not [string]::IsNullOrWhiteSpace($relativePath)) {
            $absolutePath = Join-Path $repoRoot $relativePath

            if (-not (Test-Path -LiteralPath $absolutePath)) {
                $errors.Add("Line ${lineNumber}: $field points to a missing path: $relativePath")
            }
        }
    }
}

if ($rows.Count -gt 0) {
    $actualColumns = $rows[0].PSObject.Properties.Name

    foreach ($column in $expectedApplicationColumns) {
        if ($actualColumns -notcontains $column) {
            $errors.Add("applications.csv is missing expected column '$column'.")
        }
    }
}

$rows |
    Group-Object duplicate_check_key |
    Where-Object { -not [string]::IsNullOrWhiteSpace($_.Name) -and $_.Count -gt 1 } |
    ForEach-Object {
        $ids = ($_.Group | ForEach-Object { $_.application_id }) -join ", "
        $errors.Add("Duplicate duplicate_check_key '$($_.Name)' in applications: $ids.")
    }

$eventCount = 0

if (Test-Path -LiteralPath $EventsPath) {
    $events = Import-Csv -LiteralPath $EventsPath
    $eventCount = $events.Count
    $applicationIds = @{}

    foreach ($row in $rows) {
        $applicationIds[$row.application_id] = $true
    }

    for ($i = 0; $i -lt $events.Count; $i++) {
        $event = $events[$i]
        $lineNumber = $i + 2

        foreach ($field in $eventRequiredFields) {
            if ([string]::IsNullOrWhiteSpace($event.$field)) {
                $errors.Add("application-events.csv line ${lineNumber}: missing required field '$field'.")
            }
        }

        if (-not [string]::IsNullOrWhiteSpace($event.application_id) -and -not $applicationIds.ContainsKey($event.application_id)) {
            $errors.Add("application-events.csv line ${lineNumber}: unknown application_id '$($event.application_id)'.")
        }

        if ($event.event_type -and $validEventTypes -notcontains $event.event_type) {
            $errors.Add("application-events.csv line ${lineNumber}: invalid event_type '$($event.event_type)'.")
        }

        if ($event.status_after -and $validStatuses -notcontains $event.status_after) {
            $errors.Add("application-events.csv line ${lineNumber}: invalid status_after '$($event.status_after)'.")
        }

        if (-not [string]::IsNullOrWhiteSpace($event.evidence_path)) {
            $absolutePath = Join-Path $repoRoot $event.evidence_path

            if (-not (Test-Path -LiteralPath $absolutePath)) {
                $errors.Add("application-events.csv line ${lineNumber}: evidence_path points to a missing path: $($event.evidence_path)")
            }
        }
    }

    $events |
        Group-Object event_id |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_.Name) -and $_.Count -gt 1 } |
        ForEach-Object {
            $errors.Add("Duplicate event_id '$($_.Name)' in application-events.csv.")
        }
}

if ($errors.Count -gt 0) {
    $errors | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Host "Application tracker looks good. Rows checked: $($rows.Count). Events checked: $eventCount."
