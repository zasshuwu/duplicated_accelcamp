# Project Test log
**Date:** Thursday, November 14, 2019
**Tester:** Hoang Anh

## Run environment:
```
System Information
------------------
      Time of this report: 11/14/2019, 00:17:32
             Machine name: [REDACTED]
               Machine Id: {REDACTED}
         Operating System: Windows 10 Pro 64-bit (10.0, Build 18362) (18362.19h1_release.190318-1202)
                 Language: English (Regional Setting: English)
      System Manufacturer: Micro-Star International Co., Ltd.
             System Model: MS-7B22
                     BIOS: BIOS Date: 10/09/18 15:47:02 Ver: V2.50 (type: BIOS)
                Processor: Genuine Intel(R) CPU 0000 @ 3.20GHz (12 CPUs), ~3.2GHz
                   Memory: 16384MB RAM
      Available OS Memory: 16322MB RAM
                Page File: 9320MB used, 9689MB available
              Windows Dir: C:\WINDOWS
          DirectX Version: DirectX 12
      DX Setup Parameters: Not found
         User DPI Setting: 96 DPI (100 percent)
       System DPI Setting: 96 DPI (100 percent)
          DWM DPI Scaling: Disabled
                 Miracast: Available, with HDCP
Microsoft Graphics Hybrid: Not Supported
 DirectX Database Version: Unknown
           DxDiag Version: 10.00.18362.0387 64bit Unicode
```
- Python version: 3.7.3
- All dependencies in README.md installed

## Running TestLoadPlot.pyw
- Run unsuccessful
- Break at ``` Module not found: tkinter ```
- Tried installing tkinter using ``` python3.7 -m pip install tk ```
- Break again at multiple points:
```
self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable

...

Original exception was: 
Traceback (most recent call last):
  File "TestLoadPlot.pyw", line 16, in <module>
    run = LoadRun(file)
  File "/mnt/c/Users/Nogamioka/Desktop/dev/hoanganh-dev/src/Load.py", line 46, in LoadRun
    root = Tk()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2023, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable
```
- Solution: Have not found yet as of the latest commit.

## Alternative for running TestLoadPlot.pyw
- Running in PyCharm
- Configure your PyCharm venv to install all required modules and simply run again.