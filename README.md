# Accelerometer Project
Some legends to get started:
- Annotation codes:
  - 001: convention
    - 001a: naming
    - 001b: refactoring
    - 001c: spacing
  - 002: library
    - 002a: built-in
    - 002b: user-defined
    - 002c: installed via pipelines
-----------------------------------
## Section 1: File Structure
```
.
..
/data
  | /2019 06 12
    | 0 degrees
    | 34 degrees
    | 63 degrees
  | Dataset 1
    | run#
      | run#.accel.accelModel.csv
      | run#.omega.instrument.csv
  | Dataset 2
  | Dataset 3
  | Dataset 4
  | Dataset 5
  | Spike
/doc
/src
/tools
/tutorials
Figure_1.png
Figure_2.png
Figure_12.png
Figure_9001.png
Figure_Dataset3_run1.png
ML fig.png --> #001a
README.md
unittest setup.png --> #001a
zero x.png --> #001a
```

## Section 2: Quickstart - root_dir: /src
### Formats:
***WARNING:*** The project is still not setup for out-of-the-box cross-platform execution. Therefore, directory paths are not yet configured for Apple (DARWIN) and Linux (Linux) platforms. However, a Windows PC with PyCharm installed can run the scripts rather readily. That being said, dependencies i.e., packages and modules need to be correctly configured in order to run the scripts. Refer to the list of dependencies below.

### Understanding modules and dependencies:
Based on the ```TestLoadPlot.pyw``` file in ```src``` folder, I drew up the following mapping of dependencies and modules...
- Python 3.6 and up is required. Have not tested with older versions, but Python 2.7 will definitely break.
```
tkinter (002c)*
numpy (002c)
os (002a)
Load (002b)
  | LoadAccel (002b)
    | MyFunctions --> dialogOpenFilename
    | DataStructures --> AccelData
  | LoadOmega (002b)
  | tkinter (002a)
| MyFunctions (002b)
| Plotter (002b)
```
*: tkinter has shown not working on DARWIN platform in several compatibility tests. This problem is still being investigated by the team.

### Processing and plotting raw data:
- New users who just forked the repo should running TestLoadPlot.pyw script to get started and get a taste of this whole project.
- Open up your favorite terminal/bash
- Change working directory to ```~/nameOfRepo/src/```
- Run the aforementioned script file
- Below are the example commands
```
$ cd nameOfRepo/src
$ { local_python_executable_PATH } TestLoadPlot.pyw
```
- A file-selecting dialog should pop up at this point.
- Go to and select ``` ~/data/2019 06 12/run1 ``` folder.
- Refer to the following illustrative screenshots:

**IF (ENV==DARWIN (i.e. Apple, macOS)):**

**IF (ENV==WIN32 (i.e. Windows distros)):**

**IF (ENV==LINUX (i.e. Ubuntu, etc.)):**

- The return should be a plot by matplotlib like this:

### Raw Data Collection
- Raw data collected from test devices should be named ```run#.accel.modelName.csv``` and placed in ```/data/Dataset#/run#/```
- Raw data are collected in two different ways as described in the ```/tutorials/doc/AccelCamp Tutorial.docx``` file

