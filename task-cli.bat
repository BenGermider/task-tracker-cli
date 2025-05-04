@echo off
setlocal
set SCRIPT_DIR=%~dp0
set PYTHONPATH=%SCRIPT_DIR%
python "%SCRIPT_DIR%main.py" %*
endlocal
