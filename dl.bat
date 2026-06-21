curl --ssl-no-revoke -o zipped https://codeload.github.com/azazelcodes/temp/zip/refs/heads/gaming || exit /b 1
"C:\Program Files\7-Zip\7z.exe" x zipped || exit /b 1
del /q zipped
move temp-gaming/binne .
rmdir /s /q temp-gaming

echo user_pref("security.fileuri.strict_origin_policy", false); >> %APPDATA%\Mozilla\Firefox\Profiles\LHMS\prefs.js
python serve.py
