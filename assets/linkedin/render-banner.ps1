$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# Renders the LinkedIn banner (1584 x 396) with flat typography. Text is kept out of the
# bottom-left, where the profile photo overlaps the banner on desktop and mobile.

Add-Type -AssemblyName System.Drawing

$outputDir = Join-Path $PSScriptRoot 'generated'
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

function New-Brush([string]$hex) {
    return [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($hex))
}

function New-Pen([string]$hex, [float]$width = 1) {
    return [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml($hex), $width)
}

function Add-Text {
    param(
        [System.Drawing.Graphics]$Graphics,
        [string]$Text,
        [System.Drawing.Font]$Font,
        [System.Drawing.Brush]$Brush,
        [float]$X,
        [float]$Y,
        [float]$Width,
        [float]$Height,
        [System.Drawing.StringAlignment]$Alignment = [System.Drawing.StringAlignment]::Near
    )

    $format = [System.Drawing.StringFormat]::new()
    $format.Alignment = $Alignment
    $format.LineAlignment = [System.Drawing.StringAlignment]::Near
    $format.Trimming = [System.Drawing.StringTrimming]::None
    $format.FormatFlags = [System.Drawing.StringFormatFlags]::NoWrap
    $rect = [System.Drawing.RectangleF]::new($X, $Y, $Width, $Height)
    $Graphics.DrawString($Text, $Font, $Brush, $rect, $format)
    $format.Dispose()
}

$fonts = @{
    Label = [System.Drawing.Font]::new('Segoe UI Semibold', 24, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
    Big = [System.Drawing.Font]::new('Segoe UI Semibold', 56, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
    Chip = [System.Drawing.Font]::new('Segoe UI', 24, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
    Url = [System.Drawing.Font]::new('Segoe UI', 22, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
}

$palette = @{ Background = '#131A17'; Ink = '#F4F0E8'; Muted = '#A9B3AC'; Accent = '#5FCB94'; Line = '#2C3A34' }

$banners = @(
    [pscustomobject]@{
        File = 'linkedin-banner-a.png'
        Label = 'AI/ML ENGINEER  ·  PRODUCTION AI SYSTEMS'
        Line1 = 'Use AI for judgment calls.'
        Line2 = 'Use code for anything that must be exact.'
    }
)

$chipRow1 = 'LLM search over 2M+ auto parts   ·   Serverless data pipelines on AWS'
$chipRow2 = 'MLOps: deploys from 3 hours to 15 minutes   ·   Organizer, Daejeon Global Tech Coffee'
$url = 'azizjonkasimov.github.io'

foreach ($banner in $banners) {
    $bitmap = [System.Drawing.Bitmap]::new(1584, 396)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $graphics.Clear([System.Drawing.ColorTranslator]::FromHtml($palette.Background))

    $inkBrush = New-Brush $palette.Ink
    $mutedBrush = New-Brush $palette.Muted
    $accentBrush = New-Brush $palette.Accent
    $linePen = New-Pen $palette.Line 2

    # Label row with accent bar, top-left (safe on every layout).
    $graphics.FillRectangle($accentBrush, 72, 44, 10, 30)
    Add-Text $graphics $banner.Label $fonts.Label $accentBrush 98 44 1000 34
    Add-Text $graphics $url $fonts.Url $mutedBrush 1000 46 512 32 ([System.Drawing.StringAlignment]::Far)

    # Two big lines; bottom edge stays above y=210 so the mobile photo overlap never covers them.
    Add-Text $graphics $banner.Line1 $fonts.Big $inkBrush 72 88 1440 70
    Add-Text $graphics $banner.Line2 $fonts.Big $inkBrush 72 148 1440 70

    # Proof chips, right of the photo zone (x >= 560).
    $graphics.DrawLine($linePen, 560, 262, 1512, 262)
    Add-Text $graphics $chipRow1 $fonts.Chip $mutedBrush 560 282 960 34
    Add-Text $graphics $chipRow2 $fonts.Chip $mutedBrush 560 322 960 34

    # Report measured widths so overflow is caught without opening the image.
    foreach ($pair in @(@($banner.Line1, $fonts.Big), @($banner.Line2, $fonts.Big), @($chipRow1, $fonts.Chip), @($chipRow2, $fonts.Chip))) {
        $size = $graphics.MeasureString($pair[0], $pair[1])
        Write-Output ("{0,-70} width={1:N0}" -f $pair[0], $size.Width)
    }

    $path = Join-Path $outputDir $banner.File
    $bitmap.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)

    $linePen.Dispose()
    $inkBrush.Dispose()
    $mutedBrush.Dispose()
    $accentBrush.Dispose()
    $graphics.Dispose()
    $bitmap.Dispose()
}

$fonts.Values | ForEach-Object { $_.Dispose() }
Get-ChildItem -Path $outputDir -Filter '*.png' | Select-Object Name, Length
