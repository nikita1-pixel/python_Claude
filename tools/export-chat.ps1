# export-chat.ps1
# Converts the latest Claude Code JSONL transcript into a readable markdown file.
# Run at session end: powershell -File tools\export-chat.ps1
# Output: sessions\YYYY-MM-DD-raw-chat.md

$transcriptDir = "C:\Users\nirma\.claude\projects\C--Users-nirma-OneDrive-Desktop-python-python-Claude"
$outputDir     = "C:\Users\nirma\OneDrive\Desktop\python\python_Claude\sessions"

$latest = Get-ChildItem $transcriptDir -Filter "*.jsonl" |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1

if (-not $latest) { Write-Host "No transcript found."; exit 1 }

$lines  = Get-Content $latest.FullName -Encoding utf8
$today  = Get-Date -Format "yyyy-MM-dd"
$outPath = "$outputDir\$today-raw-chat.md"

$output      = [System.Collections.Generic.List[string]]::new()
$exchangeNum = 0

$output.Add("# Raw Session -- $today")
$output.Add("")
$output.Add("> Word-for-word conversation. Nikita = learner, Claude = mentor.")
$output.Add("> Tool calls and file writes are stripped -- only the actual chat is here.")
$output.Add("")
$output.Add("---")
$output.Add("")

foreach ($line in $lines) {
    try { $obj = $line | ConvertFrom-Json -ErrorAction Stop } catch { continue }

    # User typed messages (skip tool result entries)
    if ($obj.type -eq "user" -and $obj.message.role -eq "user") {
        $c = $obj.message.content
        $text = ""
        if ($c -is [string]) { $text = $c.Trim() }
        elseif ($c -is [array]) {
            $text = ($c | Where-Object { $_.type -eq "text" } | ForEach-Object { $_.text }) -join "`n"
            $text = $text.Trim()
        }
        if ($text -ne "") {
            $exchangeNum++
            $ts = if ($obj.timestamp) { [datetime]$obj.timestamp | Get-Date -Format "HH:mm" } else { "" }
            $output.Add("### [$exchangeNum] Nikita  $ts")
            $output.Add("")
            $output.Add($text)
            $output.Add("")
        }
    }

    # Assistant text messages (skip tool_use blocks)
    elseif ($obj.type -eq "assistant" -and $obj.message.role -eq "assistant") {
        $c = $obj.message.content
        $text = ""
        if ($c -is [string]) { $text = $c.Trim() }
        elseif ($c -is [array]) {
            $text = ($c | Where-Object { $_.type -eq "text" } | ForEach-Object { $_.text }) -join "`n"
            $text = $text.Trim()
        }
        if ($text -ne "") {
            $ts = if ($obj.timestamp) { [datetime]$obj.timestamp | Get-Date -Format "HH:mm" } else { "" }
            $output.Add("### Claude  $ts")
            $output.Add("")
            $output.Add($text)
            $output.Add("")
            $output.Add("---")
            $output.Add("")
        }
    }
}

$output.Add("*End -- $exchangeNum user exchanges.*")
$output | Out-File -FilePath $outPath -Encoding utf8
Write-Host "Saved: $outPath  ($exchangeNum exchanges)"
