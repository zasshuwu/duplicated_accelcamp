import numpy as np
from DataStructures import AccelData

def GenADot(_AccelData:AccelData):
    adot_list = np.array([])
    dt = _AccelData.t[1]-_AccelData.t[0]
    for i in range(len(_AccelData.a[0])-1):
        adot_list = np.array(list(adot_list)+[(_AccelData.a[1][i+1]-_AccelData.a[1][i])/dt])
    return adot_list

def Genyx2(_AccelData:AccelData):
    olist = (np.square(_AccelData.a[0])*_AccelData.a[1])[:-1]
    return olist