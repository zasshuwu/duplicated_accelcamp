import numpy
import matplotlib
from MyFunctions import *
from Load_A import * #Pseudo to be changed with LoadAccel
myOpts = {}
myOpts['initialfile'] = 'TopRight_Feb18.csv'
'''Test file was TopRight_Feb18.csv'''
fullPathName = dialogOpenFilename(myOpts)
a = LoadRaw_3(fullPathName)
print(a)

time = a[0]
ax = a[1]
ay = a[2]
def graphing():
    """display graphs before user times"""
    avg_ax = np.average(ax)
    avg_ay = np.average(ay)
    print("The average acceleration in x is %s\nThe average acceleration in y is %s" %(avg_ax,avg_ay))
    #plt.title('raw data: close window to show RMS analysis')
    plt.subplot(2,1,1)
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
    plt.ioff()
    plt.show()