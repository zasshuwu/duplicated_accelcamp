import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from MyFunctions import *
from Load import *

#fullPathName = 'C:\\Users\\Jeff\Documents\\GitHub\\2019_06_AccelerationCamp\\data\\Spike\\DATA-017.csv'
r=Load_X2()
a= r.a #a[0] is time
time= r.t

time2 = list(filter(lambda x : x < 8, list(time)))
ax = a[0][:len(time2)]
ay= a[1][:len(time2)]

mag = np.sqrt(np.square(ax)+np.square(ay))

abs_mag= np.absolute(ax)
#abs_y= np.absolute(ay)

#time_x = np.argmax(abs_y)]
print(np.amax(abs_mag))
#print(np.amax(abs_y))
print("Time of max a " + str(time[np.argmax(abs_mag)]))
#print("Time of max " + str(time[np.argmax(abs_y)]))

plt.subplot(2, 1, 1)
plt.plot(time2,mag, label="Accel in x")
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel("Time")
plt.ylabel("Acceleration in x-direction")
ax_mean = [np.mean(mag)]*len(time2)
ax_mean_line = plt.plot(time2,ax_mean, label='Mean', linestyle='--')
plt.legend(['Acceleration in x', 'Average in x'])

'''plt.subplot(2,1,2)
plt.subplots_adjust(hspace=0.3)
plt.plot(time2,ay, label='Accel in y')
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel("Time")
plt.ylabel("Acceleration in y-direction")
ay_mean = [np.mean(ay)]*len(time2)
ay_mean_line = plt.plot(time2,ay_mean, label='Mean', linestyle='--')
plt.legend(['Acceleration in y', 'Average in y'])'''
plt.show()