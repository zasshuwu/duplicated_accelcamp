import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["savefig.dpi"] = 250
from DataStructures import *
import numpy as np
from datetime import date

class MultiTimeSeriesPlotter:
    def __init__( self, _nbPlots, _tArray):
        self.tArray = _tArray
        self.nbPlots = _nbPlots
        self.iPlot = 0

        return

    def applyStyle(self):
        plt.subplots_adjust(hspace=0.07)
        plt.xlim(0, np.max(self.tArray))
        plt.minorticks_on()
        plt.grid(b=True, which='major', color='0.65', linestyle='-', linewidth='1.0')
        plt.grid(b=True, which='minor', color='0.65', linestyle='-', linewidth='0.2')
        plt.gca().set_xticklabels([])

# yAxisLabel must be in double quotes eg "A_x ($m/s^2$)"
    def appendSignal(self, _array, yAxisLabel):
        self.iPlot=self.iPlot+1
        plt.subplot(self.nbPlots, 1, self.iPlot)

        undersize = np.size(self.tArray)-np.size(_array)
        if undersize>0:
            np.pad(_array, (0, undersize), 'constant', constant_values=1)
        elif undersize<0:
            print("Error: MultiTimeSeriesPlotter: length of appendSignal > self.tArray")
            print( "Error details: label for appending signal ", yAxisLabel)
            exit(1)

        plt.plot(self.tArray, _array)
        plt.ylabel(yAxisLabel, fontsize=8)

        self.applyStyle()
        return

    def display(self):
        plt.draw()
        plt.show()




def Plot(AccelDatas, RotaryDatas):
    tArray = RotaryDatas[0].t
    a = AccelDatas[0].a
    omegaArray = RotaryDatas[0].omega

    myPlotter = MultiTimeSeriesPlotter(3, tArray )

    myPlotter.appendSignal(a[0],"A_x ($m/s^2$)")
    myPlotter.appendSignal(a[1], "A_y ($m/s^2$)")
    myPlotter.appendSignal(omegaArray, "omega (rad/s)")

    myPlotter.display()

def Curv_plot(ar,at,r, loss, time):
    fig = plt.figure()
    plt.subplot(4, 1, 1)
    plt.plot(time, ar)
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65', linestyle='-')
    plt.xlabel("Time")
    plt.xlim([0, np.max(time)])
    plt.gca().set_xticklabels([])

    plt.subplot(4, 1, 2)
    plt.subplots_adjust(hspace=05.0)
    plt.plot(time, at, label='Accel in y')
    plt.minorticks_on()
    plt.grid(b=True, which='both', color='0.65', linestyle='-')
    plt.xlabel("Time")
    plt.xlim([0, np.max(time)])
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