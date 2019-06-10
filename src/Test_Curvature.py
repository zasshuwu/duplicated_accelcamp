from Load import *
from Plotter import *
from Curvature import *
import matplotlib.pyplot as plt

_range = [13, 18]

acceldat = LoadRun()["accel"][0]

mask = np.logical_not((_range[0] <= acceldat.t[:-1]) ^ (_range[1] >= acceldat.t[:-1]))

adot = GenADot(acceldat)[mask]
yx2 = Genyx2(acceldat)[mask]

plt.scatter(yx2, np.square(adot))
plt.show()
