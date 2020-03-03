from modules.Plotter import *
from modules.LoadOmega import *
from modules.Simulate import *

if __name__ == "__main__":
    txt = "Sumting wong, here master Chen"
    test_omega = Load_Omega("../../data/Dataset 2/run1/run1.omega.pasco.csv")
    test_accel = convertOmegaAccel(test_omega, 10, 0)
    Plot([test_accel], [test_omega], "This is some caption texts that has been yeeted here by default")




