from modules.LoadOmega import *
from modules.Simulate import *
from modules.Cluster import *
from modules.LoadAccel import *
from modules.Plotter import *
import csv

import matplotlib.animation as anime
from matplotlib import style
import random


selection = 2 # File selection with tkinter on macOS is not working as expected therefore use default direct path to data file

if __name__ == "__main__" and selection is 1:  # manually choose run file

    captionText = input("Drop your fire caption: ") + " (user input by variable)"
    # use convertOmegaAccel because Load_Accel is not working correctly

else : # default run file no user interaction
    captionText = "Caption 1 lorem ipsum lorem ipsum\nLorem ipsum on another line.\nYet again another lorem ipsum."



captionValues = {
    "alpha": 10,
    "r": 11,
    "accel": 1293.123,
    "omega": 123476.231,
    "faux1": 63453.36158,
    "faux2": 5649846213,
}

radius = 2
test_omega2 = Load_Omega("../../data/Dataset 3/run1/run1.omega.pasco.csv")
test_accel2 = AccelData_CreateFromRotary( test_omega2, radius )

plotter = MultiPlotter_CreateFromRotaryAndAccel( test_omega2, test_accel2)

plotter.setTitle("This is the title for Test_Plotter.py")
plotter.setCaptionText(captionText)
plotter.setCaptionValues(captionValues)
plotter.display()

# direct caption injection
if(0): # bypass for now

    test_omega = Load_Omega("../../data/Dataset 2/run1/run1.omega.pasco.csv")
    test_accel = AccelData_Rotate(AccelData_CreateFromRotary(test_omega, 10), 0)
    Plot([test_accel], [test_omega], "Caption 2 lorem ipsum lorem ipsum")

# Dumping csv file

test_omega = Load_Omega("../../data/Dataset 3/run1/run1.omega.pasco.csv")
test_accel = AccelData_Rotate(
    AccelData_CreateFromRotary(
        Load_Omega("../../data/Dataset 3/run1/run1.omega.pasco.csv"),
        20
    ),
    2
)

if(0): # skipping this option for now..

    filename = input("Enter file name: ")
    with open("../../data/DumpCSV/" +filename+".csv", 'w', newline='') as csv_file:
        print("Dump file "+filename+" created...")
<<<<<<< HEAD
    np.savetxt('../../data/DumpCSV/'+filename+".csv", np.c_[np.asarray(vars(test_omega)["omega"], dtype=np.float32), np.asarray(vars(test_omega)["t"], dtype=np.float32)], delimiter=",", fmt="%1.3f")

    # with open("../../data/DumpCSV/accel_dump.txt") as reimport:
    #     print(reimport)
=======
    np.savetxt('../../data/DumpCSV/'+filename+".csv", np.c_[np.asarray(vars(test_omega)["omega"], dtype=np.float32), np.asarray(vars(test_omega)["t"], dtype=np.float32)], delimiter=", ", fmt="%1.3f")

# with open("../../data/DumpCSV/accel_dump.txt") as reimport:
#     print(reimport)
>>>>>>> dev
