<div class="header">
  <h1>Inertia Sensing Lab</h1>
  <a href="https://isLab.ca">https://isLab.ca</a>
</div>

<div class="body">

# The short version
Collegial research on real life and pedagogical applications of specialized accelerometers and mobile-embedded accelerometers. `Please add content`

# The long version
The project stems from the basic trait of humans: curiosity. `Please add content`

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
`TBA`

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
- New folders (technical term: `Packages`) created under `/src` folder must initialized with a blank `__init__.py` file.
- Refrain from using `space` when naming any file or folder, as it could confuse whatever OS you are developing with. Use CamelCase or underscore_style instead.
- Use PEP8 as a guideline for formating thy codes.
- More `TBA`

## Creating Modules and Defining Functions:
- Follow PEP8 naming conventions.
- Carefully document the input and output of the functions with comments. This includes the type and which class was used to define those input and outputs.
- The function of the function. For example, to simulate a dataset or to simply process what data.
- Use comprehensive, short and descriptive name. Because not naming your cat  ``Asdfjhsv xyqwe`` follows the same logic.
- Must declare in comment functions that utilize classes and methods from other modules for easy maintenance and debugging.
- Example: `TBA`

## Defining local and global variables:
- Follow PEP8 naming conventions
- Again, same with defining functions, remember to document the type and how it is used within your codes.

# How to contribute
`Please add content`

# License
MIT or Creative Commons. Your choice. ``TBA``

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