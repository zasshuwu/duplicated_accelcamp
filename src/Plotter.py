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
    avg_ax = np.average(ax)
    avg_ay = np.average(ay)
    print("The average acceleration in x is %s\nThe average acceleration in y is %s" %(avg_ax,avg_ay))
    #plt.title('raw data: close window to show RMS analysis')
    fig = plt.figure()
    plt.subplot(3,1,1)
    plt.plot(time,ax, label="Accel in x")
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.xlabel("Time")
    plt.ylabel("Acceleration in x-direction")
    plt.ylabel("Acceleration in y-direction", fontsize=8)

    plt.subplot(3,1,2)
    plt.subplots_adjust(hspace=05.0)
    plt.plot(time,ay, label='Accel in y')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.xlabel("Time")
    plt.ylabel("Accel in y-direction", fontsize=8)
    plt.set_xlim(bottom=0)

    plt.subplot(3,1,3)
    plt.subplots_adjust(hspace=01.0)
    plt.plot(om_time,om_vel, label='Angular Velocity')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.xlabel("Time")
    plt.ylabel("Angular Velocity", fontsize=8)
    #plt.show(block=False)
    plt.draw()
#    plt.show(block=False)
 #   plt.pause()
    plt.show()
    '''
    try:
        Start = input("Starting time")
        End = input("End time")
        Start_int = int(Start)
        End_int = int(End)
        print("Start is %s seconds\nEnd is %s seconds" % (Start, End))
    except ValueError:
        print("A time was not entered")
        Start = input("Starting time")
        End = input("End time")

    plt.clf()
    n = 0
    avg_x = 0
    avg_x_2 = ax[(time > Start_int) & (time < End_int)].mean()
    print("method 1: " + str(avg_x))
    print("method 2: " + str(avg_x_2))

    file = pd.read_excel('C:\\Users\\Jeff\\Downloads\\charging.xlsx', header=1, sheet_name=0, index_col=4)

    x = np.arange(0, 235.5, 0.5)  # needs to be fixed to take in the x values of the excel file
    y = file.iloc[:, 1]  # takes first voltage column
    z = file.iloc[:, 2]  # takes second voltage column
    a = file.iloc[:, 3]  # takes third voltage column
    plt.plot(x, y)  # plots time v voltage
    plt.plot(x, z)  # plots time v voltage
    plt.plot(x, a)  # plots time v voltage

    plt.show()'''

