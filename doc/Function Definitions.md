# Function Definitions

## Load.py
- LoadDataSet(...)
    - _Loads multiple runs in a data set directory_
    - Input: `string` _dirpath_ (Optional)
    - Output: `[ AccelData[], RotaryData[] ]`
    
- LoadRun(...)
    - _Loads a single run directory_
    - Input: `string` _dirpath_ (Optional)
    - Output: `[ AccelData[], RotaryData[] ]`
    
## LoadAccel.py
- LoadAccelFile(...)
    - _Loads a single acceleration data file_
    - Input: `string` _filepath_
    - Output: `AccelData`
    
- Load_{Model}(...)
    - _Loads a single acceleration data file of the specified model_
    - Input: `string` _filepath_
    - Output: `AccelData`
    
## LoadOmega.py
- Load_Omega(...)
    - _Loads a single omega data file_
    - Input: `string` _filepath_
    - Output: `RotaryData`
    
## Curvature.py
- GenADot(...)
    - _Generates the first order derivative of the acceleration data_
    - Input: `AccelData`
    - Output: `double[]`
    
- Genyx2(...)
    - _Does y*x^2 for the given acceleration data_
    - Input: `AccelData`
    - Output: `double[]`
    
## SpikeTracker.py
- SpikeAdjust(...)
    - _Align given data to a spike_
    - Input: `AccelData[]`, `RotaryData[]`
    - Output: `AccelData[]`, `RotaryData[]`
    
- FindSpike(...)
    - _Finds the time of the spike in the given data_
    - Input: `AccelData` or `RotaryData`
    - Output: `double`

- TrimSets(...)
    - _Resampling of the data sets_
    - Input: `AccelData[]`, `RotaryData[]`
    - Output: `AccelData[]`, `RotaryData[]`
    
## MyFunctions.py
- dialogOpenFilename(...)
    - _Opens a dialog box and gives the path of the selected file_
    - Input: `dictionary` _usrOptions_
    - Output: `string` filepath
    
- min_lambda(...)
    - _Finds the minimum item using a given criteria_
    - Input: `function` _key_, `iterable` array
    - Outputs: `obj`
    
## Plotter.py
- Plot(...)
    - _Plots the given data on a graph_ **ASSUMING SAME TIME AXIS FOR ALL GIVEN DATA**
    - Input: `AccelData[]`, `RotaryData[]`
    - Output: `None`
    
## Simulate.py
- simConstAlpha(...)
    - _Generates a synthetic `RotaryData`_
    - Input:
        - `int` _N_ (number of data points)
        - `float` _deltaT_ 
        - `float` _alpha_
        - `float` _omega\_0_ (initial omega point)
    - Output: `RotaryData`
    
- convertOmegaAccel(...)
    - _Generate a synthetic `AccelData` from a `RotaryData`_
    - Input: `RotaryData`, `float` radius
    - Output: `AccelData`
