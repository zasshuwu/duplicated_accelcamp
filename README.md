Important note to developers when creating new files and folders:<br> 
Please refrain from using spaces in naming to avoid the inconvenience of referencing those names in future development. Instead, thou art highly encouraged to use the shish-kebab style `abc-def-ghi` or camelCase `thisIsAnExampleFile` (however, we mainly use this camelCase for writing code inn Python).

Note: Does not include semantically-named functions

The following documentation lists all the modules (functions within the modules) and necessary dependencies installed from package managers:

## Project-defined modules
```
# Working directory: ./src/
# User-defined modules and child functions/class:
- CopyFile.py
- Curvature.py
  - GenADot()
  - Genyx2()
- DataStructures.py (Deprecated)
- DataStructuresNew.py
  - isVec3()
  - isArrayofVec3()
  - assertIsArrayOfVec3()
  - isScalarArrayOfDoubles()
  - AccelData (class)
    - getSingleAxis()
  - RotaryData (class)
  - test_DataStructures()
- integrateDifferentialEquations.py
  - modelSHM()
  - modelSHMCoulomb()
  - model()
- InteractivePlots.py
  - LineBuilder (class)
- Load.py
  - LoadDataSet()
  - LoadRun()
- LoadAccel.py
  - LoadAccelFile()
  - Load_Any()
  - Load_X()
  - Load_Samsung()
  - Load_X16()
  - Load_X2()
  - Load_Pocket()
- LoadOmega.py
  - Load_Omega()
- MyFunctions.py
  - plottest()
  - LoadArray_GCDCBlue()
  - LoadArray()
  - runningAverage()
  - dialogOpenFilename()
  - min_lambda()
- Plotter.py
  - MultiPlotter (class)
    - applyStyle()
    - appendSignal()
    - display()
  - Plot()
  - Curv_Plot()
- Pseudo.py
  - LoadRaw_1()
  - LoadRaw_2()
  - LoadRaw_3()
- radius.py
- Simulate.py
  - simConstAlpha()
  - convertOmegaAccel()
- SpikeTracker.py
  - SpikeAdjust()
- Test_Curvature.py 
- test_main.py (testing module, omitted)
- Test_SpikePlot.py
- Test1.py
- TestLoadPlot.pyw
- UpdateSVN.py
- xSmoothingAnalysis.py
- xViewRawData
```

## Dependencies: 
Modules that you either need to import or install via package managers
```
sys (Python)
os (Python)
shutil (Python)
datetime (Python)
unittest (Python testing module)
----------------
numpy (3rd-party)
matplotlib (3rd-party)
tkinter (3rd-party)
scipy (3rd-party)
```
