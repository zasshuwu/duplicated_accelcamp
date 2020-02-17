from Load import *
from Plotter import *
from Curvature import *
from Simulate import *
import matplotlib.pyplot as plt

_range = [13, 18]
if __name__ == "__main__":
    use_range = True if input("use time range? (y/n): ") == "y" else False
    use_synthetic_data = True if input("use synthetic data? (y/n): ") == "y" else False
    if use_range:
        _range = [float(input("Beginning: ")), float(input("End: "))]

    if use_synthetic_data:
        if True if input("use omega file? (y/n): ") == "y" else False:
            o = LoadRun()["omega"][0]
        else:
            o = simAlpha(
                int(input("Number of iterations: ")),
                np.float32(input("Delta t: ")),
                np.float32(input("alpha: ")),
                np.float32(input("omega at t=0: "))
            )
        acceldat = convertOmegaAccel(o, np.float32(input("Radius: ")))
    else:
        acceldat = LoadRun()["accel"][0]

else:
    use_range = False
    use_synthetic_data = False
    acceldat = LoadAccelFile("../../data/2019 06 12/0 degrees/run1/run1.accel.x2.CSV")

if use_range:
    mask = np.logical_not((_range[0] <= acceldat.t[:-1]) ^ (_range[1] >= acceldat.t[:-1]))
else:
    mask = np.array([True]*len(acceldat.t[:(-1 if not use_synthetic_data else -2)]))

adot = GenADot(acceldat)[mask]
yx2 = Genyx2(acceldat)[mask]


if __name__ != "__main__":
    def close_event():
        plt.close() #timer calls this function after 3 seconds and closes the window

    fig = plt.figure()
    timer = fig.canvas.new_timer(interval = 1000) #creating a timer object and setting an interval of 3000 milliseconds
    timer.add_callback(close_event)

    timer.start()
plt.scatter(yx2, np.square(adot))
plt.show()
