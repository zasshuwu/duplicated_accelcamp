"""
    This was created to replace the clustered Plotter.py and to seamlessly integrate Multi and Poly.
"""

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["savefig.dpi"] = 250
matplotlib.rcParams["figure.figsize"] = 9, 7

import numpy as np
from datetime import date

class MultiPlotter:
    def __init__(self, _nbPlots, _tArray, _xLabel):
        self.tArray = _tArray
        self.nbPlots = _nbPlots
        self.iPlot = 0
        self.xLabel = _xLabel
        self.fig = plt.figure()
        self.fig.text(0.1, 0.9, date.today())

    def setTitle(self, string, loc):
        self.fig.suptitle(string, loc=loc)
    
    def applyStyle(self):
        plt.subplots_adjust(hspace=0.2, bottom=0.3)
        plt.xlim(0, np.max(self.tArray))
        plt.minorticks_on()
        plt.grid(b=True, which='major', color='0.65', linestyle='-', linewidth='1.0')
        plt.grid(b=True, which='minor', color='0.65', linestyle='-', linewidth='0.2')

    def appendSignal(self, _array, yAxisLabel="", title=""):
        self.iPlot = self.iPlot + 1
        ax = plt.subplot(self.nbPlots, 1, self.iPlot)

        undersize = np.size(self.tArray) - np.size(_array)
        if undersize > 0:
            _array = np.pad(_array, (0, undersize), 'constant', constant_values=0)
        elif undersize < 0:
            _array = _array[:len(_array) + undersize]

        plt.plot(self.tArray, _array)
        plt.ylabel(yAxisLabel, fontsize=8)
        ax.set_title(title, loc='right', pad=-.01, fontsize=7)

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
    
    # these cosmetics and file ouput are currently not implemented to reduce cluster when integrating the multiplotter and polyplotter

    # def dumpToCSVFile(self, filename="defaultTest"):
    #     with open('../../data/DumpCSV/'+filename+'.csv', 'w', newline='')
    
    def addCaption(self, txt):
        plt.figtext(0.1, 0.05, txt, fontsize=9)
        return

    def appendCaptionValues(self, value_dict):
        return

    def display(self):
        plt.draw()
        plt.show()

    class MPSignal:
        def __init__(self, array, yLabel):
            self.array = array
            self.yLabel = yLabel
            return
        
    class MultiPlotterAggregator:
        def __init__(self, tArray, xLabel):
            self.tArray = tArray
            self.xLabel = xLabel
            self.signals = []
            return

        def newSignal(self, yLabel):
            array = []
            self.signals.append(MultiPlotter.MPSignal(array, yLabel))
            return array
        
        def bindSignal(self, array, yLabel):
            self.signals.append(MultiPlotter.MPSignal(array, yLabel))
            return array

        def display(self):
            N = len(self.signals)
            mp = MultiPlotter(N, self.tArray, self.xLabel)
            for i in range(N):
                s = self.signals[i]
                mp.appendSignal(s.array, s.yLabel)
            plt.show()

        def displayPoly(self):
            for signal in self.signals:
                plt.plot(self.tArray, signal.array)
            plt.show()

def MPPlot(AccelDatas, RotaryDatas):

    tArray = RotaryDatas[0].t
    plot = MultiPlotter.MultiPlotterAggregator(tArray, "Time, t(s)")
    for omega in RotaryDatas:
        plot.bindSignal(omega.omega, "omega (rad/s)")
    
    for accel in AccelDatas:
        plot.bindSignal(accel.getSingleAxis(axisIndex=0), "$A_x (m/s^2)$")
        plot.bindSignal(accel.getSingleAxis(axisIndex=1), "$A_y (m/s^2)$")
    
    plot.display()

def PPPlot(xarray, *yarrays):

    plot = MultiPlotter.MultiPlotterAggregator(xarray, "X")
    for yarray in yarrays:
        plot.quitbindSignal(yarray, '')
    plot.displayPoly()