from Load import *
from Plotter import *
from Curvature import *
import matplotlib.pyplot as plt

acceldat = LoadRun()["accel"][0]
adot = GenADot(acceldat)
yx2 = Genyx2(acceldat)

plt.scatter(yx2,adot)
plt.show()