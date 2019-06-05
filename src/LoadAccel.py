import numpy as np
import os
from MyFunctions import dialogOpenFilename
from DataStructures import AccelData

Model_Dict = {
    "X2":"Load_X2(",
    "X16":"Load_X16(",
    "Samsung":"Load_Samsung("
}

def Load_X(filepath = None):
    if(filepath == None):
        filepath = dialogOpenFilename()
    
    block = np.loadtxt(filepath, dtype=float, comments= ";", delimiter=',', usecols=(0,1,2,3), unpack=True)
    #a = [ax, ay, az] | t = [t]
    a = block[1:]
    t = block[0]
    t0 = t[0]
    for y in range(len(t)):
        t[y]-=t0

    return AccelData(a, t, 64)

def Load_Samsung(filepath = None):
    if(filepath == None):
        filepath = dialogOpenFilename()
    
    block = np.loadtxt(filepath, dtype=float, delimiter=',', usecols=(0,1,2,3), unpack=True, skiprows=1)
    #a = [ax, ay, az] | t = [t]
    a = block[1:]
    t = block[0]
    t0 = t[0]
    for y in range(len(t)):
        t[y]-=t0

    a *= 9.807    
    return AccelData(a, t, 64)

def Load_X16(filepath = None):
    #Since Load_X works with X16s, it just returns Load_X()
    data = Load_X(filepath)
    return data

def Load_X2(filepath = None):
    #Since Load_X works with X2s, it just returns Load_X()
    #Assuming X2 has High Gain (counts/13108)
    data = Load_X(filepath)

    data.a /= 13108
    data.a *= 9.807
    
    return data

def Load_Any(model,filepath=""):
    try:
        return eval(Model_Dict[model]+"'"+filepath+"')")
    except KeyError:
        return "Model is not currently supported"

