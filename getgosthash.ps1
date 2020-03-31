# This script is used to get sha256 hash of gost files.

$version = '2.11.0'
$url32 = "https://github.com/ginuerzh/gost/releases/download/v$version/gost-windows-386-$version.zip"
$url64 = "https://github.com/ginuerzh/gost/releases/download/v$version/gost-windows-amd64-$version.zip"

$gost32file = 'gost32.zip'
$gost64file = 'gost64.zip'
Invoke-WebRequest $url32 -OutFile $gost32file
Invoke-WebRequest $url64 -OutFile $gost64file

$hash32 = (Get-FileHash $gost32file -Algorithm SHA256).Hash
$hash64 = (Get-FileHash $gost64file -Algorithm SHA256).Hash

Write-Output """url"":""$url32"","
Write-Output """hash"":""$hash32"""
Write-Output """url"":""$url64"","
Write-Output """hash"":""$hash64"""

Remove-Item -Path $gost32file, $gost64file