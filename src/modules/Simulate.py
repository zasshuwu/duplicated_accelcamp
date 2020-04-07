from modules import Tools
from modules.DataStructures import *
from modules.Cluster import *
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
    try:
        float(alphaFn(0))  # if A can be converted to a float, this won't raise an Error
    except:
        raise ValueError('alphaFn must be a function that returns a single number')

    omega = np.array([np.double(omegaInitial)] * N)
    time = np.array([np.double(0.0)] * N)
    for i in range(1, N):
        omega[i] = omega[i - 1] + alphaFn(i * deltaT) * deltaT  # small check to verify the value of typeofA
        time[i] = i * deltaT

    return RotaryData(time, omega)

# returns nothing: rotData itself is modified
def RotaryData_AddNoise( rotData: RotaryData, magnitude: float ):
    return RotaryData(rotData.t, rotData.omega + np.random.normal(0, magnitude, len(rotData))) 

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


def AccelData_CreateFromRotary2( rotData : RotaryData, radius : float):
    deltaT = rotData.t[1] - rotData.t[0]
    a = []
    for i in range(len(rotData) - 1):
        arfoo = rotData.omega[i] ** 2 * radius
        arnextfoo = rotData.omega[i+1] ** 2 * radius
        atfoo = radius * (rotData.omega[i + 1] - rotData.omega[i]) / deltaT
        cluster = Cluster_CreateFromCell(Cell(arfoo,atfoo,deltaT), radius)
        # print(cluster.ar_next - arnextfoo)
        # print(cluster.costDeltaOmega(4))
        a.append([
                arfoo,
                atfoo,
                0
        ])

    aout = np.array(a)
    for i in range(len(a)-1):
        cluster2 = Cluster_CreateFromAccelData(AccelData(rotData.t[:-1], aout, "synthetic data"), i)
        print(cluster2.ar_next-a[i+1][0])
        print(cluster2.costDeltaOmega(4))
    return AccelData(rotData.t[:-1], aout, "synthetic data")



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

# ======================== Example for radius and alpha functions ========================
def example_radius(x): # the function must have only one input which is a number
    out = 4*x
    # stuff happens here...
    return out # the function must return a single numerical value

