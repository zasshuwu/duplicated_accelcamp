import numpy as np
import os
from Load import *
from MyFunctions import *
from Plotter import *

run = LoadRun(None if __name__ == "__main__" else "../data/2019 06 12/0 degrees/run1/")
Plot(run["accel"],  run["omega"])
