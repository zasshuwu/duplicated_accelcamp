import numpy as np
import os
from MyFunctions import *

Model_Dict = {
    "X2":"Load_X2(",
    "X16":"Load_X16(",
    "Samsung":"Load_Samsung("
}

def Load_X():
    #File Dialog Options
    myOpts = {}
    myOpts['initialfile'] = 'TopRight_Feb18.csv'
    fullPathName = dialogOpenFilename(myOpts)
    
    block = np.loadtxt(fullPathName, dtype=float, comments= ";", delimiter=',', usecols=(0,1,2,3), unpack=True)
    #a = [ax, ay, az] | t = [t]
    a = block[1:]
    t = block[0]
    t0 = t[0]
    for y in range(len(t)):
        t[y]-=t0

    #STILL NEED TO CONVERT COUNTS TO M/S2
    return a, t

def Load_Samsung():
    #File Dialog Options
    myOpts = {}
    myOpts['initialfile'] = 'TopRight_Feb18.csv'
    fullPathName = dialogOpenFilename(myOpts)
    
    block = np.loadtxt(fullPathName, dtype=float, delimiter=',', usecols=(0,1,2,3), unpack=True, skiprows=1)
    #a = [ax, ay, az] | t = [t]
    a = block[1:]
    t = block[0]
    t0 = t[0]
    for y in range(len(t)):
        t[y]-=t0

    a *= 9.807    
    return a, t

def Load_X16():
    #Since Load_X works with X16s, it just returns Load_X()
    a,t = Load_X()

def Load_X2():
    #Since Load_X works with X2s, it just returns Load_X()
    #Assuming X2 has High Gain (counts/13108)
    a,t = Load_X()

    a /= 13108
    a *= 9.807
    
    return a,t

def Load_Any(model,params=""):
    try:
        return eval(Model_Dict[model]+params+")")
    except KeyError:
        return "Model is not currently supported"

