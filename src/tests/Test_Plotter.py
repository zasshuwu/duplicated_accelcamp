from modules.LoadOmega import *
from modules.Simulate import *
from modules.Cluster import *
from modules.LoadAccel import *
import csv


import matplotlib.animation as anime
from matplotlib import style
import random

selection = 2 # File selection with tkinter on macOS is not working as expected therefore use default direct path to data file

if __name__ == "__main__" and selection is 1:  # manually choose run file
    from modules.Plotter import *
    txt = input("Drop your fire caption: ") + " (user input by variable)"
    # use convertOmegaAccel because Load_Accel is not working correctly

    # caption injection via variable
    test_omega2 = Load_Omega()
    test_accel2 = AccelData_Rotate(AccelData_CreateFromRotary(test_omega2, random.randint(0, 10)), random.randint(0, 2))
    Plot([test_accel2], [test_omega2], txt)

    # direct caption injection
    test_omega = Load_Omega()
    test_accel = AccelData_Rotate(AccelData_CreateFromRotary(test_omega, random.randint(0, 10)), random.uniform(0, 5))
    Plot([test_accel], [test_omega], "This is some caption texts that has been yeeted here by default")


    

elif __name__ == "__main__" and selection is 2:  # default run file
    from modules.Plotter import *
    txt = "Caption 1 lorem ipsum lorem ipsum\nLorem ipsum on another line.\nYet again another lorem ipsum."

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

    # Dumping csv file

    test_omega = Load_Omega("../../data/Dataset 3/run1/run1.omega.pasco.csv")
    test_accel = AccelData_Rotate(
        AccelData_CreateFromRotary(
            Load_Omega("../../data/Dataset 3/run1/run1.omega.pasco.csv"),
            20
        ),
        2
    )

    # This commented portion was me progressively testing how to dump the data ###########

    # attr_omega = vars(test_omega)
    # attr_accel = vars(test_accel)
    # print(type(attr_omega['t']))
    # print(attr_accel['a'])


    # Just to clear up the file for demo
    # dump_file_accel = open("../../data/DumpCSV/accel_dump.txt", "w")
    # dump_file_accel.write("")
    # dump_file_omega = open("../../data/DumpCSV/omega_dump.txt", "w")
    # dump_file_omega.write("")

    # Writing the files
    # dump_file = open("../../data/DumpCSV/accel_dump.txt", "a")
    # dump_file.write(str("TIME: \n" + " %s, " % attr_accel['t']))
    # dump_file = open("../../data/DumpCSV/accel_dump.txt", "a")
    # dump_file.write(str("\nACCEL: \n" + " %s, " % attr_accel['a']))
    #
    # dump_file = open("../../data/DumpCSV/omega_dump.txt", "a")
    # dump_file.write(str("TIME: \n" + " %s, " % attr_omega['t']))
    # dump_file = open("../../data/DumpCSV/omega_dump.txt", "a")
    # dump_file.write(str("\nOMEGA: \n" + " %s, " % attr_omega['omega']))

    # Writing the files as csv and compare

    # dump_csv_omega = np.asarray(attr_omega['omega'], dtype=np.float32)
    # dump_csv_time = np.asarray(attr_omega['t'], dtype=np.float32)
    # np.savetxt('../../data/DumpCSV/test_dump.csv', np.c_[dump_csv_time, dump_csv_omega], delimiter=",", fmt="%1.3f")
    # print("File dumped to CSV successfully")

    # End of testing ############
    # The shortened method can be seen below ################

    # Generalizing the dictionary call and create blank csv file for output:
    filename = input("Enter file name: ")
    with open("../../data/DumpCSV/" +filename+".csv", 'w', newline='') as csv_file:
        print("Dump file "+filename+" created...")
    np.savetxt('../../data/DumpCSV/'+filename+".csv", np.c_[np.asarray(vars(test_omega)["omega"], dtype=np.float32), np.asarray(vars(test_omega)["t"], dtype=np.float32)], delimiter=",", fmt="%1.3f")

    # with open("../../data/DumpCSV/accel_dump.txt") as reimport:
    #     print(reimport)
