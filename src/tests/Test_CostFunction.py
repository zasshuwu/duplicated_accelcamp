import numpy as np
from modules.Plotter import *
from modules.DataStructures import *

# raw 2D accelerometer data associated with a single time step
# and calculation of various other quantities derived from it
class DataCell:

    def __init__(self):
        self.ar = np.NAN
        self.at = np.NAN
        self.delta_t = np.NAN
        self.radius = np.NAN

    def setFromFloats( self, ar: float, at: float, delta_t : float, radius: float):
        self.ar=ar
        self.at=at
        self.delta_t = delta_t
        self.radius = radius
        return

    def setFromAccelData(self, ad : AccelData, i: int, radius: float ):
        a = ad.getSingleAxis(i)
        self.ar = a[0]
        self.at = a[1]
        self.delta_t = ad.t[i+1]-ad.t[i]
        return

    def setRadius(self , radius: float):
        self.radius = radius
        return



    def v(self):
        return np.sqrt(self.ar * self.radius)

    # the true v_next value based on current values
    def v_next(self):
        return self.v() + self.at * self.delta_t

    # the true ar_next value based on current values and true radius
    def ar_next(self):
        return np.square(self.v_next() ) / self.radius

    def ar_dot(self):
        return (self.ar_next()-self.ar)/self.delta_t

    def ratio(self):
        return (self.v_next() - self.v())/self.v()

    # angle, in degrees, that the total acceleration vector makes with the radial direction
    # later extension: positive angle means at and v in same direction ( speeding up )
    def AccelAngle(self):
        return 180/np.pi * np.arctan(-self.ar/self.at)

    # calculate ardot using a trial "incorrect" value for the radius
    def ar_dot_trialRadius(self,trialRadius):
        term1 = np.square(self.at) / trialRadius * self.delta_t
        term2 = 2 * self.at * np.sqrt(self.ar / trialRadius)
        #print("class cost t1,t2, ardot", term1, term2, self.ar_dot() )
        return term1 + term2

    def signed_cost(self, trialRadius):
        return self.ar_dot() - self.ar_dot_trialRadius(trialRadius)

    def cost(self, trialRadius):
        return np.square(self.signed_cost(trialRadius))


class DataCellInspector:
    def __init__(self , a : AccelData, radius : float ):
        self.a=a
        self.radius = radius
        return



# set conditions: this is for ratio = 0.1
at = 2
ar = 1
delta_t = .1
radius = 4

data1 = DataCell()
data1.setFromFloats( ar, at, delta_t, radius)


# set conditions: this is for ratio = 10
at = -100
ar = .1
delta_t = .1
radius = 4
data2 = DataCell()
data2.setFromFloats( ar, at, delta_t, radius)


# plot cost vs. radius for a single ideal data point
def PlotCost():

    data = data2
    print("delta_v / v = ", data.ratio())

    # cost
    trialRadius = np.arange(2,8,.1)
    cost = np.empty(trialRadius.size)
    i=0

    for r in trialRadius:
        cost[i]=data.cost(trialRadius[i])
        i=i+1

    plotter = MultiPlotter( 1, trialRadius, "radius")
    plotter.setTitle( "kickstart regime. Ratio = " + str(data.ratio()) + " angle: " + str(data.AccelAngle()) + " degrees" )

    plotter.appendSignal( cost, "C O S T" )
    plotter.display()
    # dict = ( val, string; val, string; val, string )
    # NOT IMPLEMNETED: plotter.addCaptionValues( captionString='', dict )
    return


PlotCost()