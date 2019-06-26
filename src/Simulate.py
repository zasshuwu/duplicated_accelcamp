from DataStructures import *
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

    return RotaryData(omega, time)

def convertOmegaAccel(OmegaData, radius):
    deltaT = OmegaData.t[1] - OmegaData.t[0]
    ar = []
    at = []
    az = []
    for i in range(OmegaData.len - 1):
        ar.append(OmegaData.omega[i] ** 2 * radius)
        at.append(radius*(OmegaData.omega[i + 1] - OmegaData.omega[i]) / deltaT)
        az.append(0)
    ar = np.array(ar)
    at = np.array(at)
    az = np.array(az)
    a_temp = np.array([at, ar, az])
    return AccelData(a_temp, OmegaData.t, "synthetic data")
