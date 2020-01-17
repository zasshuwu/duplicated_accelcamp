from DataStructuresNew import *
import numpy as np


def simConstAlpha(N, dT, A=10.0, omega_0=0.0):
    '''N is the number of iterations
    dT is the delta T
    A is the Alpha'''
    omega = np.array([omega_0]*N)
    time = np.array([0.0]*N)
    for i in range(1, N):
        omega[i] = omega[i-1]+A*dT
        time[i] = i*dT

    return RotaryData(time, omega)


def convertOmegaAccel(OmegaData, radius):
    deltaT = OmegaData.t[1] - OmegaData.t[0]
    a = []
    for i in range(OmegaData.len - 1):
        a.append([
            OmegaData.omega[i] ** 2 * radius,
            radius*(OmegaData.omega[i + 1] - OmegaData.omega[i]) / deltaT,
            0
        ])

    a = np.array(a)
    return AccelData(OmegaData.t, a, "synthetic data")
