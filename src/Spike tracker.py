import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from MyFunctions import *
from Load import *
import pandas as pd



def FindSpkieTime_run(dirpath=None):
    global mag, abs_mag, time1, ax, ay,time2,omega,abs_omega
    r = LoadRun(dirpath)
    for accel in r["accel"]:
        ad = accel
    for _omega in r["omega"]:
        od = _omega

    a = ad.a  # a[0] is time
    time1 = ad.t

    time1 = list(filter(lambda x: x < 7, list(time1)))
    ax = a[0][:len(time1)]
    ay = a[1][:len(time1)]

    mag = np.sqrt(np.square(ax) + np.square(ay))

    abs_mag = np.absolute(mag)

    b = od.omega
    time2 = od.t
    time2 = list(filter(lambda x: x < 5, list(time2)))

    omega = b[:len(time2)]
    abs_omega = np.absolute(omega)

    t1 = time1[np.argmax(abs_mag)]
    t2 = time2[np.argmax(abs_omega)]
    delta = t2 - t1
    time2 -= delta
    time2 = np.array(list(filter(lambda x: x >= 0, time2)))

    print(np.amax(abs_mag))
    print(np.amax(abs_omega))
    print("Time of max Acceleration: " + str(time1[np.argmax(abs_mag)]))
    print("Time of max Omega: " + str(time2[np.argmax(abs_omega)]))

    omega = b[:len(time2)]
    abs_omega = np.absolute(omega)

FindSpkieTime_run()











plt.subplot(2, 1, 1)
plt.plot(time1,mag, label="Accel in x")
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel("Time")
plt.ylabel("Acceleration in x-direction")
ax_mean = [np.mean(mag)]*len(time2)
ax_mean_line = plt.plot(time2,ax_mean, label='Mean', linestyle='--')
plt.legend(['Acceleration in x', 'Average in x'])

plt.subplot(2,1,2)
plt.subplots_adjust(hspace=0.3)
plt.plot(time2,omega, label='Accel in y')
plt.minorticks_on()
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel("Time")
#ay_mean_line = plt.plot(time2,, label='Mean', linestyle='--')
plt.legend(['Acceleration in omega', 'Average in omega'])
plt.show()