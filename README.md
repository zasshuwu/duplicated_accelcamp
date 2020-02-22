<div class="header" style="margin-bottom: 2rem; text-align: center;">
  <h1>Inertia Sensing Lab</h1>
  <a href="https://isLab.ca"><span style="background: grey; color: black; font-size: 16pt">https://isLab.ca</span></a>
</div>

<div class="body">

# The short version
Collegial research on real life and pedagogical applications of specialized accelerometers and mobile-embedded accelerometers. <span class="block">Please add content</span>

# The long version
The project stems from the basic trait of humans: curiosity. <span class="block">Please add content</span>

# Contents
- [Features]()
- [Examples]()
  - [Handwriting map]()
  - [SpinLab]()
  - [Radius optimization]()
    - [Constant Alpha]()
    - [Varied Alpha]() (piece-wised defined, sinusoidal)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installations](#installations)
  - [Dependencies](#dependencies)
  - [Troubleshooting](#troubleshooting)
- [Project structure]()
- [Documentation]()
- [Contributing]()
- [License]()

# Features
1. Latin alphabetical handwrite grapher
2. SpinLab
3. Retrieve rotational motion parameters: alpha, r, omega
4. Optimize r using gradient descent method
5. etc

# Examples
<span class="block">TBA</span>

# Getting Started
<span class="block">TBA</span>

## Prerequisites

## Installations

## Dependencies

## Troubleshooting

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
      | Test # not tf-related
      | tfTest # tf-related
    | __init__.py
    | index.py
  | tools
  | README.md
  | .gitignore
```
# Documentation and Development

## Ground rules:
- New folders (technical term: <span class="block">packages</span>) created under ```/src``` folder must initialized with a blank ```__init__.py``` file.
- Refrain from using <span class="block">space</span> when naming any file or folder, as it could confuse whatever OS you are developing with. Use CamelCase or underscore_style instead.
- Use PEP8 as a guideline for formating thy codes.
- More <span class="block">TBA</span>

## Creating Modules and Defining Functions:
- Follow PEP8 naming conventions.
- Carefully document the input and output of the functions with comments. This includes the type and which class was used to define those input and outputs.
- The function of the function. For example, to simulate a dataset or to simply process what data.
- Use comprehensive, short and descriptive name. Because not naming your cat <span class="block"> Asdfjhsv xyqwe</span> follows the same logic.
- Must declare in comment functions that utilize classes and methods from other modules for easy maintenance and debugging.
- Example: <span class="block">TBA</span>

## Defining local and global variables:
- Follow PEP8 naming conventions
- Again, same with defining functions, remember to document the type and how it is used within your codes.

# How to contribute
<span class="block">Please add content</span>

# License
MIT or Creative Commons. Your choice. <span class="block">TBA</span>

</div>

<style>
.header h1 {
  color: #32a852;
}

h1 {
  color: #007e8a;
}

.block {
  display: inline;
  background: grey;
  font-size: 8pt;
  color: black;
  text-transform: uppercase;
  padding: 0.1rem;
  text-align: center;
}

</style>