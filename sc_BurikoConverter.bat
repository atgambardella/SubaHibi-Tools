@echo off
setlocal ENABLEDELAYEDEXPANSION
set "src=%cd%"

cd %src%\txt_scripts_en
for %%f in (%src%\txt_scripts_en\*.txt) do (
	copy !src!\raw_scripts\%%~nf "%src%\txt_scripts_en"
)

for %%f in (%src%\txt_scripts_en\*.txt) do (
	!src!\BurikoConverter.exe -e "%%~nf"
)

for %%f in (%src%\txt_scripts_en\*.txt) do (
	del /q "!src!\txt_scripts_en\%%~nf"
)

for %%f in (%src%\txt_scripts_en\*.new) do (
	move %%f !src!\encoded_scripts
)
cd /d "!src!\encoded_scripts"

for %%f in (%src%\encoded_scripts\*.new) do (
	set file=%%f
	move %%f !file:~0,-4!
)
pause