import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from MyFunctions import *
from Load import *

#fullPathName = 'C:\\Users\\Jeff\Documents\\GitHub\\2019_06_AccelerationCamp\\data\\Spike\\DATA-017.csv'
r=LoadRun()
a= r["accel"][0].a #a[0] is time
time= r["accel"][0].t
ax = a[0]
ay= a[1]

abs_x= np.absolute(ax)
abs_y= np.absolute(ay)

#time_x = np.argmax(abs_y)]
print(np.amax(abs_x))
print(np.amax(abs_y))
print(time[np.argmax(abs_x)])
print(time[np.argmax(abs_y)])

plt.subplot(2, 1, 1)
plt.plot(time,ax, label="Accel in x")
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel("Time")
plt.ylabel("Acceleration in x-direction")
ax_mean = [np.mean(ax)]*len(time)
ax_mean_line = plt.plot(time,ax_mean, label='Mean', linestyle='--')
plt.legend(['Acceleration in x', 'Average in x'])
plt.subplot(2,1,2)
plt.subplots_adjust(hspace=0.3)
plt.plot(time,ay, label='Accel in y')
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel("Time")
plt.ylabel("Acceleration in y-direction")
ay_mean = [np.mean(ay)]*len(time)
ay_mean_line = plt.plot(time,ay_mean, label='Mean', linestyle='--')
plt.legend(['Acceleration in y', 'Average in y'])
#plt.pause(10)
plt.show()