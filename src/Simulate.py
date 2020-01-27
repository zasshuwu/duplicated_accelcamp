from DataStructuresNew import *
import numpy as np


def simConstAlpha(N, dT, A=10.0, omega_0=0.0):
    """
    :param N: number of iterations
    :param dT: delta t
    :param A: alpha
    :param omega_0: intial omega value
    :return:
    """
    omega = np.array([np.double(omega_0)]*N)
    time = np.array([np.double(0.0)]*N)
    for i in range(1, N):
        omega[i] = omega[i-1]+A*dT
        time[i] = i*dT

    return RotaryData(time, omega)


def convertOmegaAccel(OmegaData, radius):
    """
    :param OmegaData: data to base the accel data on
    :param radius: radius of apparatus
    :return:
    """
    deltaT = OmegaData.t[1] - OmegaData.t[0]
    a = []
    for i in range(len(OmegaData) - 1):
        a.append([
            OmegaData.omega[i] ** 2 * radius,
            radius*(OmegaData.omega[i + 1] - OmegaData.omega[i]) / deltaT,
            0
        ])

    a = np.array(a)
    return AccelData(OmegaData.t[:-1], a, "synthetic data")
