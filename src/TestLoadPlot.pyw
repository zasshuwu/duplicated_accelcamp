import numpy as np
import os
from Load import *
from MyFunctions import *
from Plotter import *

run = LoadRun()
Plot(run["accel"],  run["omega"])
