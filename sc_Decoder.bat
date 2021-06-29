@echo off
setlocal ENABLEDELAYEDEXPANSION
set "src=F:\_visual-novels\_projects\subahibi_script_tools"

for %%f in (%src%\raw_scripts\*) do (
	BurikoConverter.exe -d %%f
	echo %%f
)
for %%f in (%src%\raw_scripts\*.txt) do (
	move %%f %src%\txt_scripts_jp
)
cd /d "%src%\encoded_scripts"
pause