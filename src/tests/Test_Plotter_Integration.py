import os, os.path
import sys
import random
import platform
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import LoadOmega, Cluster, Simulate, Plotter_Integration

if str(platform.system()) == 'Linux':
    omega = LoadOmega.Load_Omega("../../data/Dataset 2/run2/run2.omega.pasco.csv")
else:
    messagebox.showinfo("ALERT", "Select an omega dataset from data/dataset/")
    try:
        omega = LoadOmega.Load_Omega()
    except:
        print("No files were chosen. Exiting with code 69-420-247...")

accel = Simulate.AccelData_Rotate(Simulate.AccelData_CreateFromRotary(omega, random.randint(0, 10)),
                                  random.randint(0, 2))

Plotter_Integration.MPPlot([accel], [omega])

a = []

for i in range(100):
    a.append([random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)])

Plotter_Integration.PPPlot(*a)
