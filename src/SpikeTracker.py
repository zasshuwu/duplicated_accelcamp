import numpy as np
from DataStructures import *

adjust = 0.5

def SpikeAdjust(_AccelDatas, _RotaryDatas):
    global adjust
    AccelDatas = _AccelDatas
    RotaryDatas = _RotaryDatas

    time_list = []
    min_t_list = None
    min_t_list_spike = None
    '''================Acceleration================='''
    for ad in AccelDatas:
        a = ad.a  # a[0] is time
        time1 = ad.t
        time1 = list(filter(lambda x: x < 7, list(time1)))
        ax = a[0][:len(time1)]
        ay = a[1][:len(time1)]

        mag = np.sqrt(np.square(ax) + np.square(ay))

        abs_mag = np.absolute(mag)
        time_list.append(time1[np.argmax(abs_mag)])
        if min_t_list is None:
            min_t_list = ad.t
            min_t_list_spike = time1[np.argmax(abs_mag)]
        elif len(min_t_list) > len(ad.t):
            min_t_list = ad.t
            min_t_list_spike = time1[np.argmax(abs_mag)]

    '''================Omega================='''
    for od in RotaryDatas:
        b = od.omega
        time2 = od.t
        time2 = list(filter(lambda x: x < 7, list(time2)))

        omega = b[:len(time2)]
        abs_omega = np.absolute(omega)
        time_list.append(time2[np.argmax(abs_omega)])
        if min_t_list is None:
            min_t_list = od.t
            min_t_list_spike = time2[np.argmax(abs_omega)]
        elif len(min_t_list) > len(od.t):
            min_t_list = od.t
            min_t_list_spike = time2[np.argmax(abs_omega)]

    '''================Process================='''
    time_list.sort()
    min_val = time_list[0]
    adjust = min_val - adjust
    min_t_list -= (min_t_list_spike - min_val) + adjust
    for i in range(len(AccelDatas)):
        ad = AccelDatas[i]
        a = ad.a  # a[0] is time
        time1 = ad.t
        time1 = list(filter(lambda x: x < 7, list(time1)))
        ax = a[0][:len(time1)]
        ay = a[1][:len(time1)]

        mag = np.sqrt(np.square(ax) + np.square(ay))

        abs_mag = np.absolute(mag)
        delta = time1[np.argmax(abs_mag)] - min_val
        time1 = ad.t - (delta + adjust)
        z = len(list(filter(lambda x: x < 0, time1)))
        AccelDatas[i].t = np.array(list(filter(lambda x: x >= 0, time1)))
        AccelDatas[i].a = np.array([
            a[0][z:],
            a[1][z:],
            ad.a[2]
        ])

    for i in range(len(RotaryDatas)):
        od = RotaryDatas[i]
        b = od.omega
        time2 = od.t
        time2 = list(filter(lambda x: x < 7, list(time2)))

        omega = b[:len(time2)]
        abs_omega = np.absolute(omega)
        delta = time2[np.argmax(abs_omega)] - min_val
        time2 -= delta + adjust
        z = len(list(filter(lambda x: x < 0, time2)))
        RotaryDatas[i].t = np.array(list(filter(lambda x: x >= 0, time2)))
        RotaryDatas[i].omega = b[z:]

    return AccelDatas, RotaryDatas

def FindSpike(_dataset):
    data = _dataset.a if type(_dataset) == Acceldata else _dataset.o
    time_series = list(filter(lambda x: x < 7, list(_dataset.t)))

    magsqred = np.array(len(time_series))
    for axisdata in data:
        magsqred += np.square(axisdata[:len(time_series)])

    mag = np.sqrt(magsqred)

    abs_mag = np.absolute(mag)
    spike_t = time_series[np.argmax(abs_mag)]
    return spike_t

def AdjustToSpike(_dataset, _spike):
    return