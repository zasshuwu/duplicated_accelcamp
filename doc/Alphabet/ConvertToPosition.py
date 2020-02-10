from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import csv

fig = plt.figure()
ax = plt.axes(projection="3d")

# Acquires and Stores Raw Data and Convert to Acceleration
v0 = [0, 0, 0]
x0 = [0, 0, 0]
mToA = 1
error = 0.28

t = []
time = []
m = [[] for i in range(3)]
magnitude = [[] for i in range(3)]

with open("C:/Users/adamo/Documents/GitHub/The-Ascent2/2019_06_AccelerationCamp/data/Alphabet/run1/Hyphen.accel.pocket.csv", 'r+') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        t = row[0]
        m[0] = row[1]
        m[1] = row[2]
        m[2] = row[3]
        time.append(float(t))
        for i in range(0, 3):
            magnitude[i].append(float(m[i]) if abs(float(m[i])) > error else 0)
Position = open('data/Position.accel.pocket.csv', 'w+')

acceleration = [[j * mToA for j in i] for i in magnitude]

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
