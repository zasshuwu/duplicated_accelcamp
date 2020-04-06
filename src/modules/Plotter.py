import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["savefig.dpi"] = 250
matplotlib.rcParams["figure.figsize"] = 9, 7

import numpy as np
from datetime import date



# produce mutliple plots with a shared horizontal axis
# _xArray is an array of floats
class MultiPlotter:
    def __init__(self, _nbPlots, _tArray, _xLabel):
        self.tArray = _tArray
        self.nbPlots = _nbPlots
        self.iPlot = 0
        self.xLabel = _xLabel
        self.fig = plt.figure()
        self.fig.text(0.1,0.9,date.today())

    def setTitle(self,string, loc):
        self.fig.suptitle(string, loc=loc)

    def applyStyle(self):
        plt.subplots_adjust(hspace=0.2, bottom=.3)  # bottom value and caption area has positive linear relationship
        plt.xlim(0, np.max(self.tArray))
        plt.minorticks_on()
        plt.grid(b=True, which='major', color='0.65', linestyle='-', linewidth='1.0')
        plt.grid(b=True, which='minor', color='0.65', linestyle='-', linewidth='0.2')

    # yAxisLabel must be in double quotes eg "A_x ($m/s^2$)"
    def appendSignal(self, _array, yAxisLabel="", title=""):
        self.iPlot = self.iPlot + 1
        ax = plt.subplot(self.nbPlots, 1, self.iPlot)

        undersize = np.size(self.tArray) - np.size(_array)
        if undersize > 0:
            _array = np.pad(_array, (0, undersize), 'constant', constant_values=0)
        elif undersize < 0:
            _array = _array[:len(_array) + undersize]
            '''
            print("Error: MultiPlotter: length of appendSignal > self.tArray")
            print( "Error details: label for appending signal ", yAxisLabel)
            exit(1)'''

        plt.plot(self.tArray, _array)
        plt.ylabel(yAxisLabel, fontsize=8)
        ax.set_title(title, loc='right', pad=-0.01, fontsize=7)

        self.applyStyle()
        if (self.nbPlots != self.iPlot):
            plt.tick_params(
                axis='x',
                which='both',
                bottom=False,
                top=False,
                labelbottom=False
            )
            plt.gca().set_xticklabels([])
        else:
            plt.xlabel(self.xLabel)

    def dumpToCSVFile(self, filename=input("Enter file name: ")):
        with open('../../data/DumpCSV/'+filename+'.csv', 'w', newline='') as dumpcsv:
            return
        # This is not complete...
        dump_omega_self = np.asarray(omega['omega'], dtype=np.float32)
        dump_omega_time = np.asarray(omega['t'], dtype=float32)
        np.savetxt('../../data/DumpCSV/'+filename+'')
        return

    # displayed under the last graph
    def addCaption(self, txt):
        plt.figtext(0.1, 0.05, txt, fontsize=9)  # figtext(x_float, y_float, caption, ...)
        return

    # dict is a dictionary of ( string, float )
    # that will be displayed in a caption
    def appendCaptionValues(self, value_dict):
        i = 0.150
        k = 0.5
        for item in value_dict:
            # This figtext value-bound string print method is exactly how print in python2.7 works
            plt.figtext(k, i, item + ": " + str("%.1f" % value_dict[item]) + ";", color='salmon', fontsize="large")
            k += 0.250
            if k >= 1:
                k = 0.50
                i += 0.025
        return

    def display(self):
        plt.draw()
        plt.show()



# new interface for MultiPlotter,
# for now provided as a wrapper to the original
#-------------------------------------------


class MPSignal:
    def __init__(self, array, yLabel):
        self.array = array
        self.yLabel = yLabel
        return

class MultiPlotterNew:
    def __init__(self, tArray, xLabel):
        self.tArray = tArray
        self.xLabel = xLabel
        self.signals = []
        return

# signals will be displayed in the order in which they are created via
# newSignal() or bindSignal()
    def newSignal(self, yLabel ):
        array = []
        self.signals.append(MPSignal(array,yLabel))
        return array

    def bindSignal(self, array, yLabel):
        self.signals.append(MPSignal(array, yLabel))
        return array

    def dumpToCSVFile(self, filename):
        return

    # displayed under the last graph
    def addCaption(self, txt):
        plt.figtext(0.1, 0.05, txt, fontsize=9)  # figtext(x_float, y_float, caption, ...)
        return

    # dict is a dictionary of ( string, float )
    # that will be displayed in a caption
    def appendCaptionValues(self, value_dict):
        i = 0.150
        k = 0.5
        for item in value_dict:
            # This figtext value-bound string print method is exactly how print in python2.7 works
            plt.figtext(k, i, item + ": " + str("%.1f" % value_dict[item]) + ";", color='salmon', fontsize="large")
            k += 0.250
            if k >= 1:
                k = 0.50
                i += 0.025
        return

    value_dict = {
        "alpha": 10,
        "r": 11,
        "accel": 1293.123,
        "omega": 123476.231,
        "faux1": 63453.36158,
        "faux2": 5649846213,
    }

    def display(self, txt="", value_dict=value_dict):
        N = len(self.signals)
        mp = MultiPlotter(N,self.tArray,self.xLabel)
        for i in range( N ):
            s = self.signals[i]
            mp.appendSignal(s.array, s.yLabel)
        mp.addCaption(txt)
        mp.appendCaptionValues(value_dict)
        mp.display()

    def displayPoly(self):
        for signal in self.signals:
            plt.plot(self.tArray, signal.array)
        plt.show()

def Plot(AccelDatas, RotaryDatas, txt="", _dict={}):

    tArray = RotaryDatas[0].t

    # define keypair dict for parameters
    '''
    i have no idea how to extract alpha and r values from the (simulated) data, 
    but basically got it to print out the dict
    '''
    value_dict = {
        "alpha": 10,
        "r": 11,
        "accel": 1293.123,
        "omega": 123476.231,
        "faux1": 63453.36158,
        "faux2": 5649846213,
    }

   # myPlotter = MultiPlotter(len(AccelDatas) * 2 + len(RotaryDatas), tArray, "Time t (s) ")
    myPlotter = MultiPlotterNew(tArray, "Time, t(s) ")
    for omega in RotaryDatas:
        myPlotter.bindSignal(omega.omega, "omega (rad/s)") #, "Pasco")

    for accel in AccelDatas:
        myPlotter.bindSignal(accel.getSingleAxis(axisIndex=0), "$A_x (m/s^2)$") #, accel.model)
        myPlotter.bindSignal(accel.getSingleAxis(axisIndex=1), "$A_y (m/s^2)$")#, accel.model)

    # myPlotter.display().addCaption(txt)  # txt is blank by default until specified.
    # myPlotter.display().appendCaptionValues(value_dict) # print parameter list
    myPlotter.display(txt, value_dict)

# # def Curv_plot(ar, at, r, loss, time):
#     fig = plt.figure()
#     plt.subplot(4, 1, 1)
#     plt.plot(time, ar)
#     plt.minorticks_on()
#     plt.grid(b=True, which='both', color='0.65', linestyle='-')
#     plt.xlabel("Time")
#     plt.xlim([0, np.max(time)])
#     plt.gca().set_xticklabels([])

#     plt.subplot(4, 1, 2)
#     plt.subplots_adjust(hspace=05.0)
#     plt.plot(time, at, label='Accel in y')
#     plt.minorticks_on()
#     plt.grid(b=True, which='both', color='0.65', linestyle='-')
#     plt.xlabel("Time")
#     plt.xlim([0, np.max(time)])
#     plt.gca().set_xticklabels([])

#     plt.subplot(4, 1, 3)
#     plt.subplots_adjust(hspace=01.0)
#     plt.plot(time, r, label='Angular Velocity')
#     plt.minorticks_on()
#     plt.grid(b=True, which='both', color='0.65', linestyle='-')
#     plt.xlabel("Time")
#     plt.xlim([0, np.max(time)])
#     # plt.show(block=False)
#     plt.subplot(4, 1, 4)
#     plt.subplots_adjust(hspace=01.0)
#     plt.plot(time, loss, label='Angular Velocity')
#     plt.minorticks_on()
#     plt.grid(b=True, which='both', color='0.65', linestyle='-')
#     plt.xlabel("Time")
#     plt.xlim([0, np.max(time)])
#     plt.gca().set_xticklabels([])
#     plt.draw()
#     #    plt.show(block=False)
#     #   plt.pause()
#     plt.show()