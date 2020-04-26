import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["savefig.dpi"] = 250
matplotlib.rcParams["figure.figsize"] = 9, 7

import numpy as np
from datetime import date


class MPSignal:
    def __init__(self, array, yLabel):
        self.array = array
        self.yLabel = yLabel
        return


class MultiPlotter:
    def __init__(self, tArray, xLabel):
        self.tArray = tArray
        self.xLabel = xLabel
        self.signals = []
        self.iPlot = 0
        self.captionValues = {}
        self.captionText = ""
        return

    def applyStyle(self):
        plt.subplots_adjust(hspace=0.2, bottom=.3)  # bottom value and caption area has positive linear relationship
        plt.xlim(0, np.max(self.tArray))
        plt.minorticks_on()
        plt.grid(b=True, which='major', color='0.65', linestyle='-', linewidth='1.0')
        plt.grid(b=True, which='minor', color='0.65', linestyle='-', linewidth='0.2')

    # signals will be displayed in the order in which they are created via
    # newSignal() or bindSignal()
    def newSignal(self, yLabel):
        array = []
        self.signals.append(MPSignal(array, yLabel))
        return array

    #   when using displayPoly() , yLabel ignored
    def bindSignal(self, array, yLabel=""):
        self.signals.append(MPSignal(array, yLabel))
        return array

    def dumpToCSVFile(self, filename):
        return

    # displayed under the last graph
    def setCaptionText(self, txt):
        self.captionText = txt

    # dict is a dictionary of ( string, float )
    # that will be displayed in a caption
    def setCaptionValues(self, value_dict):
        self.captionValues = value_dict

    def internal_drawCaptionText(self, txt):
        plt.figtext(0.1, 0.05, txt, fontsize=9)  # figtext(x_float, y_float, caption, ...)
        return

    def internal_drawCaptionValues(self, value_dict):
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

    def internal_applyStyle(self):
        plt.subplots_adjust(hspace=0.2, bottom=.3)  # bottom value and caption area has positive linear relationship
        plt.xlim(0, np.max(self.tArray))
        plt.minorticks_on()
        plt.grid(b=True, which='major', color='0.65', linestyle='-', linewidth='1.0')
        plt.grid(b=True, which='minor', color='0.65', linestyle='-', linewidth='0.2')

    # yAxisLabel must be in double quotes eg "A_x ($m/s^2$)"
    def internal_plotSignal(self, _array, yAxisLabel="", title=""):
        self.iPlot = self.iPlot + 1
        ax = plt.subplot(len(self.signals), 1, self.iPlot)

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

        self.internal_applyStyle()
        if (len(self.signals) != self.iPlot):
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

    def display(self):
        N = len(self.signals)

        for i in range(N):
            s = self.signals[i]
            self.internal_plotSignal(s.array, s.yLabel)

        self.internal_drawCaptionValues(self.captionValues)
        self.internal_drawCaptionText(self.captionText)
        plt.draw()
        plt.show()

    def displayPoly(self, yAxisLabel):
        for signal in self.signals:
            plt.plot(self.tArray, signal.array)
        plt.show()

    def dumpToCSVFile(self, filename):
        #    def dumpToCSVFile(self, filename=input("Enter file name: ")#):
        with open('../../data/DumpCSV/' + filename + '.csv', 'w', newline='') as dumpcsv:
            return
        # This is not complete...
        dump_omega_self = np.asarray(omega['omega'], dtype=np.float32)
        dump_omega_time = np.asarray(omega['t'], dtype=float32)
        np.savetxt('../../data/DumpCSV/' + filename + '')
        return

    #   need a default value for its "loc" location..
    def setTitle(self, string):
        plt.suptitle(string)
        return


# --------- extra service functions ------------
from modules.DataStructures import *


def MultiPlotter_CreateFromRotaryAndAccel(rd: RotaryData, ad: AccelData):
    mp = MultiPlotter(rd.t, "time t (s)")
    mp.bindSignal(rd.omega, "omega (rad/s)")  # , "Pasco")
    mp.bindSignal(ad.getSingleAxis(axisIndex=0), "$A_x (m/s^2)$")  # , accel.model)
    mp.bindSignal(ad.getSingleAxis(axisIndex=1), "$A_y (m/s^2)$")  # , accel.model)
    return mp
