from modules import Tools
from modules.DataStructures import *
import math


# region Generic AlphaSim Functions
def AlphaSim_ConstOmegaPositive():
    return


def AlphaSim_ConstOmegaChangesSign():
    return


def AlphaSim_Piecewise1(t):
    if t < 0:
        return 1
    elif 0 <= t < 0.5:
        return 0.5
    elif 0.5 <= t < 1:
        return 0.25
    elif 1 <= t:
        return 0.5


def AlphaSim_Piecewise2(t):
    if t < -2:
        return t * 1.5
    elif -2 <= t < 5:
        return math.sin(t)
    elif 5 <= t < 7:
        return 0.5
    elif 7 <= t:
        return math.cos(t)


def AlphaSim_Sinusoidal1(t):
    A = 2
    omega = 1
    phaseConstant = 0
    return A * math.sin(omega * t + phaseConstant)


def AlphaSim_GenerateAlphaArray(alphaFunc, N, deltaT):
    typeofA = 'f'
    try:
        alphaFunc(0)
        typeofA = 'f'
    except:
        try:
            alphaFunc = float(alphaFunc)
            typeofA = 'n'
        except:
            raise ValueError('A must be a function or a number')

    array = []
    for i in range(N):
        array.append(alphaFunc(i * deltaT) if typeofA == 'f' else alphaFunc)
    return array


# endregion


# region Module Functions
def simAlpha(N, dT, A, omega_0=0.0, noise=(0, 0)):
    """
    :param noise: (loc, scale)
    :param N: number of iterations
    :param dT: delta t
    :param A: alpha *can be either a float or a function*
    :param omega_0: initial omega value
    :return:
    """
    typeofA = 'f'
    try:
        A(0)
        typeofA = 'f'
    except:
        try:
            A = float(A)
            typeofA = 'n'
        except:
            raise ValueError('A must be a function or a number')

    omega = np.array([np.double(omega_0)] * N)
    time = np.array([np.double(0.0)] * N)
    for i in range(1, N):
        omega[i] = omega[i - 1] + (A if typeofA == 'n' else A(i * dT)) * dT
        time[i] = i * dT

    return RotaryData(time, omega + np.random.normal(noise[0], noise[1], len(omega)))


def convertOmegaAccel(OmegaData, radius, phi=0, noise=(0, 0)):
    """
    :param phi: angle of accelerometer
    :param noise: (loc, scale)
    :param OmegaData: data to base the accel data on
    :param radius: radius of apparatus
    :return:
    """
    typeofrad = 'f'
    try:
        radius(0)
        typeofrad = 'f'
    except:
        try:
            radius = float(radius)
            typeofrad = 'n'
        except:
            raise ValueError('radius must be a function or a number')

    deltaT = OmegaData.t[1] - OmegaData.t[0]
    a = []
    for i in range(len(OmegaData) - 1):
        rotated = Tools.rotate_vec3(
            [
                OmegaData.omega[i] ** 2 * (radius if typeofrad == 'n' else radius(OmegaData.t[i])),
                radius * (OmegaData.omega[i + 1] - OmegaData.omega[i]) / deltaT,
                0
            ],
            phi
        )
        a.append(
            rotated.tolist()[0]
        )

    a = np.array(a) + np.array([
        np.random.normal(noise[0], noise[1], len(a)),
        np.random.normal(noise[0], noise[1], len(a)),
        np.random.normal(noise[0], noise[1], len(a))
    ]).transpose()
    return AccelData(OmegaData.t[:-1], a, "synthetic data")
# endregion
