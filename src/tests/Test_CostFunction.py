import numpy as np
from modules.Cluster import *
from modules.Plotter import *
from modules.LoadAccel import *
from modules.Simulate import *

# set conditions: this is for ratio = 0.1
at = 2
ar = 1
delta_t = .1
radius = 4

cell1 = Cell(ar, at, delta_t)
cluster1 = Cluster_CreateFromCell(cell1, radius)

# set conditions: this is for ratio = 10
at = -100
ar = .1
delta_t = .1
radius = 4

cell2 = Cell(ar, at, delta_t)
cluster2 = Cluster_CreateFromCell(cell2, radius)


# plot cost vs. radius for a single ideal data point
def PlotCost():
    cluster = cluster1
    print("delta_v / v = ", cluster.delta_v_over_v(radius))

    # cost
    trialRadius = np.arange(2, 8, .1)
    cost = np.empty(trialRadius.size)
    i = 0

    for r in trialRadius:
        cost[i] = cluster2.cost(trialRadius[i])
        i = i + 1

    plotter = MultiPlotter(1, trialRadius, "radius")
    # plotter.setTitle( "kickstart regime. Ratio = " + str(cluster.delta_v_over_v(radius)) + " angle: " + str(cluster.cell.accelAngle()) + " degrees" )

    plotter.appendSignal(cost, "C O S T")
    plotter.display()
    # dict = ( val, string; val, string; val, string )
    # NOT IMPLEMNETED: plotter.addCaptionValues( captionString='', dict )
    return


def MultiPlotCost(_AccelData, step: int = 1):
    trialRadii = np.arange(0, 30, .1)
    mp = MultiPlotter( trialRadii, "Radius")
    mp.setCaptionText("caption here")
    for ri in range(0, len(_AccelData) - 1, step):
        index = ri
        current_cluster = Cluster_CreateFromAccelData(_AccelData, index)
        cost = np.empty(trialRadii.size)
        for i in range(len(trialRadii)):
            cost[i] = current_cluster.cost(trialRadii[i])
        mp.bindSignal(cost)

    # customize the x-y range before calling display()
    plt.ylim(0, 200)
    plt.xlim(0, 8)

    mp.displayPoly("cost")

# fn is a function taking one argument
# which is the values in array range
def plotCostFunction(cluster, radii):
    cost = np.empty(trialRadius.size)
    i = 0
    for r in radii:
        cost[i] = cluster.cost(radii[i])
        i = i + 1


load = False
if __name__ == "__main__":
    if not load:
        def alphaF(x):
            return np.cos(x) if x >= 2 else 1


        test_data = AccelData_CreateFromRotary(RotaryData_CreateFromAlphaFunction(alphaF, 52, 0.1), 4)
        # test_data.AddNoise(0.1)
    else:
        test_data = LoadAccelFile()

    MultiPlotCost(test_data, 10)
    # PlotCost()
