import sys

sys.path.append("../")

from tests.Izk import *
import numpy as np


# -------- Simple polar plot -------------------
def sample():
    # Graph Parameters
    n = 10000  # number of points
    f = 10  # number of lobes
    r = 5  # scaling factor (radius)
    # Data
    # numpy.linspace = linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
    theta = np.linspace(0, 2.0*np.pi,n)
    curve = r*np.cos(f*theta)

    # Get an axis handle/object
    ax1 = plt.subplot(111, polar=True)

    # Plotting
    ax1.plot(theta, curve)

    # plt.show()

# -------- Applying to our graphing ------------

# -------- Proof of concept with synthetically generated data ---------
def conceptual():
    true_phi = 2.0
    true_r = 3.0
    phi = []
    r = []
    n = 100
    loss = 1.0

    # generate synthetic phi and r
    for i in range(1, n):
        phi.append(i)
        # print(phi)
    for j in range(1, n):
        r.append(j)
        # print(r)

    # graph into polar plot

conceptual()