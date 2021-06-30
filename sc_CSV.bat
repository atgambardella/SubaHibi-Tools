@echo off

echo "Are you sure you wish to make new jp_translation.csv? (y)"
set /p inp=">"
if %inp%==y GOTO make_csv
pause
exit


:make_csv
python translate.py --make_csv "jp_translation.csv"

pause
