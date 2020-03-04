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

# alphaFn is always a function
# constant-value alpha is accomplished by feeding a const-value function
# return a RotaryData object
def RotaryData_CreateFromAlphaFunction( alphaFn,  N, deltaT, omegaInitial=0, ):
    typeofA = 'f'
    # This variable is a flag for the type of the variable A
    # 'f' means that A is of type 'function'
    # 'n' means that A is a number (float, int, double, ...)
    try:
        alphaFn(0) # if A is callable, this won't raise an Error
        typeofA = 'f'
    except:
        try:
            alphaFn = float(alphaFn) # if A can be converted to a float, this won't raise an Error
            typeofA = 'n'
        except:
            raise ValueError('alphaFn must be a function or a number')

    omega = np.array([np.double(omegaInitial)] * N)
    time = np.array([np.double(0.0)] * N)
    for i in range(1, N):
        omega[i] = omega[i - 1] + (alphaFn if typeofA == 'n' else alphaFn(i * deltaT)) * deltaT # small check to verify the value of typeofA
        time[i] = i * deltaT

    return RotaryData(time, omega)

# returns nothing: rotData itself is modified
def RotaryData_AddNoise( rotData: RotaryData, magnitude: float ):
    return RotaryData(rotData.t, rotData.omega + np.random.normal(0, magnitude, len(rotData))) 

# region Module Functions
def simAlpha(N, dT, A, omega_0=0.0, noise=(0, 0)):
    """
    :param noise: (loc, scale)
    :param N: number of iterations
    :param dT: delta t
    :param A: alpha *can be either a number or a function that returns a number* <- example at the end of the script
    :param omega_0: initial omega value
    :return:
    """
    typeofA = 'f'
    # This variable is a flag for the type of the variable A
    # 'f' means that A is of type 'function'
    # 'n' means that A is a number (float, int, double, ...)
    try:
        A(0) # if A is callable, this won't raise an Error
        typeofA = 'f'
    except:
        try:
            A = float(A) # if A can be converted to a float, this won't raise an Error
            typeofA = 'n'
        except:
            raise ValueError('A must be a function or a number')

    omega = np.array([np.double(omega_0)] * N)
    time = np.array([np.double(0.0)] * N)
    for i in range(1, N):
        omega[i] = omega[i - 1] + (A if typeofA == 'n' else A(i * dT)) * dT # small check to verify the value of typeofA
        time[i] = i * dT

    return RotaryData(time, omega + np.random.normal(noise[0], noise[1], len(omega)))

# generate simulated AccelData for a sensor at radial distance of "radius"
# starting from a rotary-sensor signal "omegaData"
# returns a AccelData object
def AccelData_CreateFromRotary( rotData : RotaryData, radius : float):
    deltaT = rotData.t[1] - rotData.t[0]
    a = []
    for i in range(len(rotData) - 1):
        a.append([
                rotData.omega[i] ** 2 * radius, 
                radius * (rotData.omega[i + 1] - rotData.omega[i]) / deltaT,
                0
        ])
    a = np.array(a)
    return AccelData(rotData.t[:-1], a, "synthetic data")

# rotate all vectors counterclockwise by an amount "angle"
def AccelData_Rotate( ad : AccelData, angle : float ):
    a = ad.a
    for i in range(len(a)):
        a[i] = Tools.rotate_vec3(a[i], angle).tolist()[0]
        
    ad.a = a
    return ad

# add gaussian noise to the components on all 3 axes
def AccelDat_AddNoise( ad : AccelData, magnitude : float  ):
    ad.a += np.array([
        np.random.normal(0, magnitude, len(a)),
        np.random.normal(0, magnitude, len(a)),
        np.random.normal(0, magnitude, len(a))
    ]).transpose()
    return ad

def convertOmegaAccel(OmegaData, radius, phi=0, noise=(0, 0)):
    """
    :param phi: angle of accelerometer
    :param noise: (loc, scale)
    :param OmegaData: data to base the accel data on
    :param radius: radius of rotation ***MUST BE EITHER A NUMBER OR A FUNCTION THAT RETURNS A NUMBER*** <- example at the end of the script
    :return:
    """
    typeofrad = 'f' 
    # This variable is a flag for the type of the variable radius
    # 'f' means that radius is of type 'function'
    # 'n' means that radius is a number (float, int, double, ...)
    try:
        radius(0) # if radius is callable, this won't raise an Error
        typeofrad = 'f'
    except:
        try:
            radius = float(radius) # if radius can be converted to a float, this won't raise an Error
            typeofrad = 'n'
        except:
            raise ValueError('radius must be a function or a number')

    deltaT = OmegaData.t[1] - OmegaData.t[0]
    a = []
    for i in range(len(OmegaData) - 1):
        radius = radius if typeofrad == 'n' else radius(OmegaData.t[i]) # small check to verify the value of typeofrad
        rotated = Tools.rotate_vec3(
            [
                OmegaData.omega[i] ** 2 * radius, 
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

# ======================== Example for radius and alpha functions ========================
def example_radius(x): # the function must have only one input which is a number
    out = 4*x
    # stuff happens here...
    return out # the function must return a single numerical value

