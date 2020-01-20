# 1. Development Environment Related
## Output your system information to diagnose problems relating to specific OS and hardware
To display your own system information, please refer to the instructions below.

- For Ubuntu/Linux:
```
$ hostnamectl
```

- For Apple macOS:
```
$ SPSoftwareDataType
```

- For Microsoft Windows:
```
1. Windows Key + R
2. Type "dxdiag" into dialog box
3. Press Enter  
```

**Please send us a bug ticket on GitHub with the system information screen capture and the error traceback that you encountered.**

# 2. tkinter related
This is where probably most of your problems arise when trying to run Python files in the [src](../src) folder. So, it is going to be a single topic of its own. We are constantly trying to snuff out bugs regarding this particular module, so we appreciate any error reports from you.

## a. macOS/DARWIN

Running Python v3.6.3 prepackaged with macOS Catalina before applying solution. [More info](hoanganh-dev-notes/fri-nov8-19.md).

**Solution steps:**
- Step 0: Open terminal
- Step 1: Install brew package manager if not already.
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
- Step 2: Change current user permission for Python folders on your macOS environment. Input your sudo password when prompted.
```
$ sudo chown -R $(whoami) /usr/local/lib/pkgconfig /usr/local/share/info /usr/local/share/man/man3 /usr/local/share/man/man5
```
```
$ chmod u+w /usr/local/lib/pkgconfig /usr/local/share/info /usr/local/share/man/man3 /usr/local/share/man/man5
```
- Step 3: Install the latest Python distribution (3.7.5)
```
$ brew install python3
```
- Step 4 (optional): Re-install dependencies when prompted with 
```
... no module <module name>
```
by running the script below
```
$ python3 -m pip install <module name 1> <module name 2> ...
```

## b. Windows
This applies for matplotlib and .pyw dialogs depending on tkinter

Running Python v3.7.x. [More info](hoanganh-dev-notes/thu-nov21-19.md).

**If you're trying to run from a shell.**

**Solutions:** 
1. Install Xming X Server for Windows
https://sourceforge.com/projects/xming/

2. Install VcXsrv Windows X Server
https://sourceforge.com/projects/vcxsrv

3. Click Windows button to bring up the Windows Start Menu

4. Search for xlaunch.exe and Run it.

5. On the dialog window, choose multiple windows. Click Next until finish.

6. Using Windows Subsystem for Linux terminal, type in:
```
export DISPLAY=localhost:0.0
```
and hit Enter

7. Now the backends can be run without GUI errors.

Alternatively, you can run the scripts in [PyCharm IDE](https://www.jetbrains.com/pycharm/download) with Python 3.6.x interpreter and later configured for your development environment.

## c. Ubuntu/Linux
&rightarrow; Yet to yield errors on this OS.
