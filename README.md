<<<<<<< HEAD
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

=======
<div class="header">
  <h1>Inertia Sensing Lab</h1>
  <a href="https://isLab.ca">https://isLab.ca</a>
</div>

<div class="body">

# The short version
Collegial research on real life and pedagogical applications of specialized accelerometers and mobile-embedded accelerometers.

# The long version
Professor Larnder initially started this project to find and further study many applications with accelerometers in mobile devices. With the newfound knowledge of how these accelerometers function in the experimental settings, we can hope to computationally develop tools from such knowledge with Python and to create new ways to teach introductory Physics for college students who can relate well with the mobile devices being at the center of the demonstrative experiment.

The research project also aims to introduce college students from basic to intermediate programming concepts and computer interactions, both of which the Cegep/college-level specifically and the university-level more generally programs currently lack thereof. These few first impressions can help potential future computer science/engineering students realize their interests and passions early on during their mileage at university. And let's be honest, in today's society, knowing, maybe only a little bit, about computer and programming can help further one's education and career path a very long way.

# Contents
- [Features](#features)
- [Examples](#examples)
  - [Handwriting map](#latin-alphabetical-handwrite-grapher)
  - [SpinLab](#spin-lab)
  - [Radius optimization](#optimize-r-using-gradient-descent-method)
    - Constant Alpha
    - Varied Alpha (piece-wised defined, sinusoidal)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installations](#installations)
  - [Dependencies](#dependencies)
  - [Troubleshooting](#troubleshooting)
- [Project structure](#project-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

# Features
`[In progress]`
1. Graph Host Object Position in 3D space
2. Handwriting Prediction
3. Object Shape Prediction

# Examples
1. ### Latin alphabetical handwrite grapher
2. ### SpinLab
3. ### Retrieve rotational motion parameters: alpha, r, omega
4. ### Optimize r using gradient descent method

# Getting Started
### Understanding the workflow 
*(Steps are both listed chronologically and in order of importance)*
- For those who are unfamiliar with our git workflow, totally new to git, or those who need a gentle reminder, this is how:
1. Assuming that you already have the repository cloned some time in the past on your device by either downloading and extracting the .zip or using the CLI.
2. Always, before start working on the codes for whatever branch, pull changes from remote branch first: `$ git pull` or click on pull function in the Github GUI.
3. After a session of adding, changing, tweaking. Always initiate a `$ git pull` before the next step to resolve incoming conflicts. (instructions on how to resolve conflicts can be found on https://git-scm.com/)
4. To add and commit changes: `$ git add . && git commit -m "<commit message>"`
5. Switch branch by `$ git checkout <branch_name>`
6. If you messed up somewhere along the way, have a backup of your changes somewhere outside the repository folder and initiate `$ git rebase` (again, website for more info).

## Prerequisites
- Intermediate knowledge of using a computer.
- Familiar with Python and computer programming flow.
- PyCharm IDE (optional for advanced users).
- Visual Code editor installed on a system with Python, Anaconda, pip. (optional for beginners).

## Installations
1. Python 3.7.x from https://python.org/ or Anaconda Python 3.7 from https://anaconda.org/distributions/ In terms of specific usage, differs with respect to OS.
2. PyCharm IDE by JetBrains. Package installation and run script are way easier with PyCharm if you are not versed in CLI.  

## Dependencies
- matplotlib
- tensorflow v1.15.0 (v2.0 WILL NOT WORK with current project syntax)
- numpy

## Troubleshooting
- Please temporarily refer to [troubleshooting.md](doc/DevNotes/hoanganh/troubleshooting.md)

# Project Structure
```
/{root}
  | data
  | doc # definitely needs some major clean up
    | Alphabet
    | AppTools
    | DevNotes
    | img
    | manuals-teardowns
    | "Position via Regression"
    | pubs
    | "PyCharm IDE Settings"
    | tutorials
    | ...
  | src
    | deprecated # we should review the modules and remove the folder soon
    | modules # all functionalities are in here
      | __init__.py
      | ...
    | tests
      | __init__.py
      | Test  # general tests
      | tfTest  # tf-related
    | __init__.py
    | index.py
  | tools
  | README.md
  | .gitignore
```
# Documentation and Development

## Ground rules:
- New folders (technical term: `Packages`) created under `/src` folder must initialized with a blank `__init__.py` file.
- Refrain from using `space` when naming any file or folder, as it could confuse whatever OS you are developing with. Use CamelCase or underscore_style instead.
- Use PEP8 as a guideline for formating thy codes.

## Creating Modules and Defining Functions:
- Follow PEP8 naming conventions.
- Carefully document the input and output of the functions with comments. This includes the type and which class was used to define those input and outputs.
- The function of the function. For example, to simulate a dataset or to simply process what data.
- Use comprehensive, short and descriptive name. Because not naming your cat  ``Asdfjhsv xyqwe`` follows the same logic.
- Must declare in comment functions that utilize classes and methods from other modules for easy maintenance and debugging.

## Defining local and global variables:
- Follow PEP8 naming conventions
- Again, same with defining functions, remember to document the type and how it is used within your codes.

# How to contribute
- Contributions from non-members can be made by forking the repository and requesting pull once you are done completing the new feature.
- Team members will review your pull request, resolve any possible conflicts, and decide either to accept or reject your request.
- Forking and pull requesting information can be found on GitHub documentations.

# License
``TBA``

</div>
>>>>>>> upstream/master
