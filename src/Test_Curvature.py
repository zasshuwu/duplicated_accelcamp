from Load import *
from Plotter import *
from Curvature import *
from Simulate import *
import matplotlib.pyplot as plt

_range = [13, 18]

use_range = True if input("use time range? (y/n): ") == "y" else False
if use_range:
    _range = [float(input("Beginning: ")), float(input("End: "))]

if True if input("use synthetic data? (y/n): ") == "y" else False:
    if True if input("use omega file? (y/n): ") == "y" else False:
        o = LoadRun()["omega"][0]
    else:
        o = simConstAlpha(
            int(input("Number of iterations: ")),
            np.float32(input("Delta t: ")),
            np.float32(input("alpha: ")),
            np.float32(input("omega at t=0: "))
        )
    acceldat = convertOmegaAccel(o, np.float32(input("Radius: ")))
else:
    acceldat = LoadRun()["accel"][0]

if use_range:
    mask = np.logical_not((_range[0] <= acceldat.t[:-1]) ^ (_range[1] >= acceldat.t[:-1]))
else:
    mask = np.array([True]*len(acceldat.t[:-2]))

#adot = GenADot(acceldat)[mask]
#yx2 = Genyx2(acceldat)[mask]

#plt.scatter(yx2, np.square(adot))
#plt.show()
