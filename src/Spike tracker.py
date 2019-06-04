import numpy as np
import matplotlib as plt
import numpy as np
from MyFunctions import *

fullPathName =
def LoadSpike(fullPathName):
    if(filepath == None):
        #File Dialog Options
        myOpts = {}
        myOpts['initialfile'] = 'TopRight_Feb18.csv'
        filepath = dialogOpenFilename(myOpts)
    # unpack makes it column-major
    block =np.loadtxt( fullPathName,dtype=float, comments= ";", delimiter=',', usecols=(0,1,2,3), unpack=True,
                       skiprows=10)
    a= block[0:] #a[0] is time
    return a

def Spike():
    plt.subplot(2,1,1)
    plt.plot(t,ax, label="Accel in x")
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    plt.xlabel("Time")
    plt.ylabel("Acceleration in x-direction")
    '''ax_mean = [np.mean(ax)]*len(time)
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
    plt.legend(['Acceleration in y', 'Average in y'])'''
    plt.ion()
    plt.show()

LoadSpike()
Spike()