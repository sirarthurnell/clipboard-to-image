@echo off
set "DESKTOP=%USERPROFILE%\Desktop"
cmd /c "cd /d %DESKTOP%\scripts\generated-apps\clipboard-to-image\venv\Scripts & .\activate & cd /d %DESKTOP%\scripts\generated-apps\clipboard-to-image & python .\main.py"