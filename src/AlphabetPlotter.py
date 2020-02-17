import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
lastIndex = len(file_path.split('/')) - 1

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
# For when the data starts at (2,1)
if file_path.split('/')[lastIndex].split('.')[2] == "pocket":
    shift_x = 2
    shift_y = 1
    error = 0.3
    fToA = 1
# For when the data starts at (0,0)
elif file_path.split('/')[lastIndex].split('.')[2] == "pocket_mobile":
    shift_x = 0
    shift_y = 0
    error = 0.3
    fToA = 1
# For when the data starts at (1,0)
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

acceleration = [[j * fToA for j in i] for i in magnitude]

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

fig, axs = plt.subplots(3)
axs[0].plot(time, acceleration[0])
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('AccelerationX (m/s^2)')
axs[1].plot(time, acceleration[1])
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('AccelerationY (m/s^2)')
axs[2].plot(position[0], position[1])
axs[2].set_xlabel('PositionX')
axs[2].set_ylabel('PositionY')
plt.show()