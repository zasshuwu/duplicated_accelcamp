import os, os.path
import sys
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import LoadOmega, Cluster, Simulate, Plotter_Integration


omega = LoadOmega.Load_Omega("../../data/Dataset 2/run2/run2.omega.pasco.csv")
accel = Simulate.AccelData_Rotate(Simulate.AccelData_CreateFromRotary(omega, random.randint(0, 10)), random.randint(0, 2))
Plotter_Integration.Plot([accel], [omega])