import Tools
from DataStructures import *


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
        omega[i] = omega[i - 1] + (A if typeofA == 'n' else A(i*dT)) * dT
        time[i] = i * dT

    return RotaryData(time, omega + np.random.normal(noise[0], noise[1], len(omega)))


def convertOmegaAccel(OmegaData, radius, phi=0, noise=(0,0)):
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
            raise ValueError('A must be a function or a number')

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
