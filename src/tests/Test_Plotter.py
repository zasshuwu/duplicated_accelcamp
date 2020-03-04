from modules.Plotter import *
from modules.LoadOmega import *
from modules.Simulate import *
import random

if __name__ == "__main__":  # manually choose run file

    txt = input("Drop your fire caption: ")
    txt += " (user input by variable)"
    # use convertOmegaAccel because Load_Accel is not working correctly

    # caption injection via variable
    test_omega2 = Load_Omega()
    test_accel2 = AccelData_Rotate(AccelData_CreateFromRotary(test_omega2, random.randint(0, 10)), random.randint(0, 2))
    Plot([test_accel2], [test_omega2], txt)

    # direct caption injection
    test_omega = Load_Omega()
    test_accel = AccelData_Rotate(AccelData_CreateFromRotary(test_omega, random.randint(0, 10)), random.uniform(0, 5))
    Plot([test_accel], [test_omega], "This is some caption texts that has been yeeted here by default")

else:  # default run file
    txt = "Caption 1 lorem ipsum lorem ipsum"

    # caption injection via variable
    test_omega2 = Load_Omega("../../data/Dataset 3/run1/run1.omega.pasco.csv")
    test_accel2 = AccelData_Rotate(
        AccelData_CreateFromRotary(
            Load_Omega("../../data/Dataset 3/run1/run1.omega.pasco.csv"),
            20
        ),
        2
    )
    Plot([test_accel2], [test_omega2], txt)

    # direct caption injection
    test_omega = Load_Omega("../../data/Dataset 2/run1/run1.omega.pasco.csv")
    test_accel = AccelData_Rotate(AccelData_CreateFromRotary(test_omega, 10), 0)
    Plot([test_accel], [test_omega], "Caption 2 lorem ipsum lorem ipsum")