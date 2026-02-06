curl -o zipped https://codeload.github.com/azazelcodes/temp/zip/refs/heads/gaming
"C:\Program Files\7-Zip\7z.exe" x zipped
del zipped
move temp-gaming/binne .
del temp-gaming

echo user_pref("security.fileuri.strict_origin_policy", false); >> %APPDATA%\Mozilla\Firefox\Profiles\LHMS\prefs.js