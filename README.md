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
`Please add content`

# Examples
`TBA`
1. ### Latin alphabetical handwrite grapher
2. ### SpinLab
3. ### Retrieve rotational motion parameters: alpha, r, omega
4. ### Optimize r using gradient descent method
5. etc

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
    | modules
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
MIT or Creative Commons. Your choice. ``TBA``

</div>
