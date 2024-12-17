@echo off

REM Chạy server trong một cửa sổ CMD mới
start "Server quan ly truong hoc" %~dp0env\python.exe manage.py runserver

REM Đếm ngược 5 giây trước khi mở trình duyệt
echo Dang khoi dong server local. Trinh duyet se mo trong 5s toi :
for /l %%i in (5,-1,1) do (
    echo %%i...
    timeout /t 1 /nobreak >nul
)

REM Mở trình duyệt trong một cửa sổ CMD mới
start "Mo trinh duyet" http://127.0.0.1:8000/

pause
