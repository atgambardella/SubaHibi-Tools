@echo off
setlocal ENABLEDELAYEDEXPANSION
setlocal ENABLEEXTENSIONS
set "src=%cd%"

cd /d "%src%\encoded_scripts"
for %%f in (%src%\raw_scripts\*) do (
	set 1=%%~nf
	if defined 1 (!src!\BurikoConverter.exe -d %%f)
)
for %%f in (%src%\raw_scripts\*.txt) do (
	move %%f %src%\txt_scripts_jp >NUL
)

pause
