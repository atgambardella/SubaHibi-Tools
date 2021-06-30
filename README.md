# 10th Mod
A mod for the 10th Anniversary Edition of Subarashiki Hibi that ports the Wonderful Everyday translation, along with an original translation of Knockin' on Heaven's Door.
I use a modified version of Gambs' scripts for Sakura no Uta translation and also EthornellEditor libraries for decoding / encoding.
Currently works well enough but it's mainly for personal usage.
I think it literally doesn't work right now without a file but I'll fix later.

## Basic usage
1. Extract script files from Subarashiki Hibi using [GARBro]https://github.com/morkt/GARbro or some similar software
2. Place them all into /raw_scripts/
3. Use BurikoConverter.exe / ScriptDecoder.bat to convert the scripts into txt files, and place into /txt_scripts_en/ if using the .exe
4. Run 'python translate.py --make_csv something.csv' or ScriptToCSV.bat
5. Import the csv data using Excel or some other software.
  1. Import it "as text", using UTF-8 / 65001.
  2. Set the delimiter to comma and have qualifier set as double quotes.
  3. Save a new CSV file as "translation.csv"
6. Modify the second row of the csv to make changes to the script
7. Use "python translate.py --make_translation_scripts" / _ScriptGenderator.bat to convert the spreadsheet into new txt files
8. If using _ScriptToBuriko.bat, place the txt files into /txt_scripts_en. otherwise just run BurikoConverter.exe to convert the new txt files into BGI scripts


* [atgambardella/sakuuta_community_challenge](https://github.com/atgambardella/sakuuta_community_challenge)
* [https://github.com/marcussacana/EthornellEditor](https://github.com/marcussacana/EthornellEditor)
