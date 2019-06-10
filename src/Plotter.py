import matplotlib.pyplot as plt
from DataStructures import *
import numpy as np


def Plot(AccelDatas, RotaryDatas):
    a = AccelDatas[0].a 
    time = AccelDatas[0].t
    ax = a[0]
    ay = a[1]

    om_time = RotaryDatas[0].t
    om_vel = RotaryDatas[0].omega
    #plt.title('raw data: close window to show RMS analysis')
    fig = plt.figure()
    plt.subplot(3,1,1)
    plt.plot(time,ax, label="Accel in x")
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.xlabel("Time")
    plt.ylabel("Acceleration in x-direction")
    plt.ylabel("Acceleration in y-direction", fontsize=8)
    plt.legend(['Accel in x','Avg in x'],loc= 0)
    plt.xlim([0,np.max(time)])

    plt.subplot(3,1,2)
    plt.subplots_adjust(hspace=05.0)
    plt.plot(time,ay, label='Accel in y')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.ylabel("Time")
    plt.ylabel("Accel in y-direction", fontsize=8)
    plt.legend(['Accel in y','Avg in y'],loc= 0)
    plt.xlim([0,np.max(time)])

    plt.subplot(3,1,3)
    plt.subplots_adjust(hspace=01.0)
    plt.plot(om_time,om_vel, label='Angular Velocity')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.xlabel("Time")
    plt.ylabel("Angular Velocity", fontsize=8)
    plt.legend(['Angular Vel','Avg Angular Vel'],loc= 0)
    plt.xlim([0,np.max(om_time)])
    #plt.show(block=False)
    plt.draw()
#    plt.show(block=False)
 #   plt.pause()
    plt.show()

def Curv_plot(ar,at,r, loss, time):
    fig = plt.figure()
    plt.subplot(4, 1, 1)
    plt.plot(time, ar)
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65', linestyle='-')
    plt.xlabel("Time")
    plt.xlim([0, np.max(time)])

    plt.subplot(4, 1, 2)
    plt.subplots_adjust(hspace=05.0)
    plt.plot(time, at, label='Accel in y')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65', linestyle='-')
    plt.xlabel("Time")
    plt.xlim([0, np.max(time)])

    plt.subplot(4, 1, 3)
    plt.subplots_adjust(hspace=01.0)
    plt.plot(time, r, label='Angular Velocity')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65', linestyle='-')
    plt.xlabel("Time")
    plt.xlim([0, np.max(time)])
    # plt.show(block=False)
    plt.subplot(4, 1, 4)
    plt.subplots_adjust(hspace=01.0)
    plt.plot(time, loss, label='Angular Velocity')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65', linestyle='-')
    plt.xlabel("Time")
    plt.xlim([0, np.max(time)])
    plt.draw()
    #    plt.show(block=False)
    #   plt.pause()
    plt.show()