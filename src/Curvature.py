import numpy as np
from DataStructuresNew import AccelData


def GenADot(_AccelData:AccelData):
    adot_list = np.array([])
    dt = _AccelData.t[1]-_AccelData.t[0]
    for i in range(len(_AccelData.getSingleAxis(0))-1):
        adot_list = np.array(list(adot_list)+[(_AccelData.getSingleAxis(1)[i+1]-_AccelData.getSingleAxis(1)[i])/dt])
    return adot_list


def Genyx2(_AccelData:AccelData):
    olist = (np.square(_AccelData.getSingleAxis(0))*_AccelData.getSingleAxis(1))[:-1]
    return olist