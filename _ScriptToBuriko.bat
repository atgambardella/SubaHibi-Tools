@echo off
setlocal ENABLEDELAYEDEXPANSION
set "src=%cd%"

cd %src%\txt_scripts_en
for %%f in (%src%\txt_scripts_en\*.txt) do (
	copy !src!\raw_scripts\%%~nf !src!\txt_scripts_en >NUL
)

for %%f in (%src%\txt_scripts_en\*.txt) do (
	!src!\BurikoConverter.exe -e "%%~nf"
)

for %%f in (%src%\txt_scripts_en\*.txt) do (
	del /q "!src!\txt_scripts_en\%%~nf" >NUL
)

for %%f in (%src%\txt_scripts_en\encode\*) do (
	move %%f !src!\encoded_scripts >NUL
)

rd "%src%\txt_scripts_en\encode"

pause
