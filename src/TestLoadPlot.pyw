import numpy as np
import os
from LoadAccel import *
from MyFunctions import *
from PlotAccel import *

run = LoadRun()
Plot(run["accel"],  run["omega"])
