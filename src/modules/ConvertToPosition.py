from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import tkinter as tk
from tkinter import filedialog

# Asking for file location with dialog box
defaultdir="../../data"
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(parent=root,initialdir=defaultdir,title='Please select a run')
lastIndex = len(file_path.split('/')) -1

fig = plt.figure()
ax = plt.axes(projection="3d")

# Acquires and Stores Raw Data and Convert to Acceleration
v0 = [0, 0, 0]
x0 = [0, 0, 0]
fToA = 1
error = 0.28

t = []
time = []
m = [[] for i in range(3)]
magnitude = [[] for i in range(3)]


shift_x = 0
shift_y = 0
if file_path.split('/')[lastIndex].split('.')[2] == "pocket":
    shift_x = 2
    shift_y = 1
    error = 0.3
    fToA = 1
elif file_path.split('/')[lastIndex].split('.')[2] == "android":
    shift_x = 0
    shift_y = 1
    error = 0.02
    fToA = 9.81

shift = 0
uselessboolean = True
with open(file_path, 'r+') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if shift < shift_y:
            shift += 1
        else:
            t = row[shift_x]
            m[0] = row[1 + shift_x]
            m[1] = row[2 + shift_x]
            m[2] = row[3 + shift_x]
            time.append(float(t))
            for i in range(0, 3):
                magnitude[i].append(float(m[i]) if abs(float(m[i])) > error else 0)

Position = open('data/'+file_path.split('/')[lastIndex].split('.')[0]+'.csv', 'w+')

acceleration = [[j * fToA for j in i] for i in magnitude]
print(acceleration)

# Translates Data into Position
velocity = [[0 for i in time] for i in range(3)]
position = [[0 for i in time] for i in range(3)]

for j in range(3):
    velocity[j][0] = v0[j]
    for i in range(1, len(time)):
        velocity[j][i] = velocity[j][i - 1] + acceleration[j][i - 1] * (time[i] - time[i - 1])
for j in range(3):
    position[j][0] = x0[j]
    for i in range(1, len(time)):
        position[j][i] = position[j][i - 1] + velocity[j][i - 1] * (time[i] - time[i - 1])
for i in range(len(position[0])):
    Position.write(str(position[0][i]))
    Position.write(',')
    Position.write(str(position[1][i]))
    Position.write(',')
    Position.write(str(position[2][i]))
    Position.write('\n')
