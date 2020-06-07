from modules.Load import *
from modules.Plotter import *

file=None

# test via manual selection of data source ( explicit run of this file alone )
if __name__ != "__main__":
    file="../../data/2019 06 12/0 degrees/run1/"

run = LoadSingleRun(file)
plotter = MultiPlotter_CreateFromRotaryAndAccel(run["omega"], run["accel"])
plotter.display()

# original code:
#run = LoadRun(None if __name__ == "__main__" else "../../data/2019 06 12/0 degrees/run1/")
#Plot(run["accel"],  run["omega"])

file=None