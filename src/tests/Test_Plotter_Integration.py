import os, os.path
import sys
import random
import platform
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import LoadOmega, Cluster, Simulate, Plotter

if str(platform.system()) == 'Linux':
    omega = LoadOmega.Load_Omega("../../data/Dataset 2/run2/run2.omega.pasco.csv")
elif str(platform.system() == 'Darwin'):
    messagebox.showinfo("Alert", "Platform is macOS - Auto load dataset")
    try:
        omega = LoadOmega.Load_Omega("../../data/Dataset 2/run2/run2.omega.pasco.csv")
        print("Loaded omega run 2 from dataset 2")
    except:
        print("Unable to load dataset. Please contact maintainer HA.")
else:
    messagebox.showinfo("ALERT", "Select an omega dataset from data/dataset/")
    try:
        omega = LoadOmega.Load_Omega()
    except:
        print("No files were chosen. Exiting with code 69-420-247...")

accel = Simulate.AccelData_Rotate(Simulate.AccelData_CreateFromRotary(omega, random.randint(0, 10)), random.randint(0, 2))

plt1 = Plotter.MultiPlotter([accel], [omega])

a = []

for i in range(100):
    a.append([random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)])

plt1.display()
