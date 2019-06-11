import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["savefig.dpi"] = 300
from DataStructures import *
import numpy as np
from datetime import date


def Plot(AccelDatas, RotaryDatas):


    a = AccelDatas[0].a 
    time = AccelDatas[0].t
    ax = a[0]
    ay = a[1]

    om_time = RotaryDatas[0].t
    om_vel = RotaryDatas[0].omega

    fig = plt.figure()

    plt.subplot(3,1,1)
    plt.title(date.today())
    plt.plot(time,ax, label="Accel in x")
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.ylabel("Accel in x ($m/s^2$)", fontsize=8)
    plt.legend(['Accel in x'],loc= 0)
    plt.xlim(0,np.max(om_time))
    plt.gca().set_xticklabels([])

    plt.subplot(3,1,2)
    plt.subplots_adjust(hspace=0.07)
    plt.plot(time,ay, label='Accel in y')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.ylabel("Accel in y ($m/s^2$)", fontsize=8)
    plt.legend(['Accel in y'],loc= 0)
    plt.xlim(0,np.max(om_time))
    plt.gca().set_xticklabels([])


    plt.subplot(3,1,3)
    plt.subplots_adjust(hspace=0.07)
    plt.plot(om_time,om_vel, label='Angular Velocity')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Velocity (rad/s)", fontsize=8)
    plt.legend(['Angular Vel'],loc= 0)
    plt.xlim(0,np.max(om_time))
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
    plt.xlim([np.max(time)])
    plt.gca().set_xticklabels([])

    plt.subplot(4, 1, 2)
    plt.subplots_adjust(hspace=05.0)
    plt.plot(time, at, label='Accel in y')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65', linestyle='-')
    plt.xlabel("Time")
    plt.xlim([np.max(time)])
    plt.gca().set_xticklabels([])

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
    plt.gca().set_xticklabels([])
    plt.draw()
    #    plt.show(block=False)
    #   plt.pause()
    plt.show()