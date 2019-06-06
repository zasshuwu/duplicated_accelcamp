echo off
cd %1
C:\Users\izk\Anaconda3\python.exe C:\Users\izk\AppData\Roaming\Microsoft\Windows\SendTo\zkStartPythonFirstCommand.py

%windir%\System32\cmd.exe "/K" C:\Users\izk\Anaconda3\Scripts\activate.bat %1

C:\Users\izk\Anaconda3\python.exe
pause
