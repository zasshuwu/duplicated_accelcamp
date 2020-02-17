import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os
import tkinter as tk
from tkinter import filedialog
from Load import *
from Tools import *
from Plotter import *

defaultdir = "../../doc/Alphabet/data"
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(parent=root,initialdir=defaultdir,title='Please select a run')

run = LoadRun(file_path)
Plot(run["accel"])

'''fig = plt.figure()
#x, y, z = np.loadtxt(file_path, delimiter=',', unpack=True)
x,y=np.loadtxt(file_path, delimiter=',')
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()'''