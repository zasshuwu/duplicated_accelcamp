import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

x, y, z = np.loadtxt('data/Position.accel.pocket.csv', delimiter=',', unpack=True)

ax1.scatter(x,y,z)
plt.show()