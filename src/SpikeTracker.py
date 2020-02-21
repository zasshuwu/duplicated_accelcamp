import numpy as np
from DataStructures import *
from scipy.signal import resample
from Tools import min_lambda

adjust = 0.5


def SpikeAdjust(_AccelDatas, _RotaryDatas):
    """ shift time axis of each data set so that the spikes are aligned.
    Does not trim the length of the data sets"""
    global adjust
    AccelDatas = _AccelDatas
    RotaryDatas = _RotaryDatas

    time_list = {}
    min_t_list = None
    min_t_list_spike = None

    '''================Acceleration================='''
    for ad in AccelDatas:
        spike_time = FindSpike(ad)

        time_list[ad] = spike_time
        # time_list is a dictionary of all timestamps for the spikes

        if min_t_list is None:  # check if we already have a minimum
            min_t_list = ad.t   # set the minimum time to this AccelData's time
            min_t_list_spike = spike_time   # set the spike timestamp

        elif len(min_t_list) > len(ad.t):  # check to see if our list is shorter than the previous minimum's
            min_t_list = ad.t   # set the minimum time to this AccelData's time
            min_t_list_spike = spike_time   # set the spike timestamp

    '''================Omega================='''
    for od in RotaryDatas:
        spike_time = FindSpike(od)

        time_list[od] = spike_time
        # time_list is a dictionary of all timestamps for the spikes

        if min_t_list is None:  # check if we already have a minimum
            min_t_list = od.t  # set the minimum time to this RotaryData's time
            min_t_list_spike = spike_time  # set the spike timestamp

        elif len(min_t_list) > len(od.t):  # check to see if our list is shorter than the previous minimum's
            min_t_list = od.t  # set the minimum time to this RotaryData's time
            min_t_list_spike = spike_time  # set the spike timestamp

    '''================Process================='''
    time3 = list(time_list.values())
    time3.sort()
    min_val = time3[0]

    adjust = min_val - adjust
    min_t_list -= (min_t_list_spike - min_val) + adjust

    for i in range(len(AccelDatas)):
        ad = AccelDatas[i]

        spike_time = time_list[ad]

        delta = spike_time - min_val
        time1 = ad.t - (delta + adjust)
        z = len(list(filter(lambda x: x < 0, time1)))

        AccelDatas[i].t = np.array(list(filter(lambda x: x >= 0, time1)))
        AccelDatas[i].a = ad.a[z:]

    for i in range(len(RotaryDatas)):
        od = RotaryDatas[i]

        spike_time = time_list[od]

        delta = spike_time - min_val
        time2 = od.t - (delta + adjust)
        z = len(list(filter(lambda x: x < 0, time2)))
        RotaryDatas[i].t = np.array(list(filter(lambda x: x >= 0, time2)))
        RotaryDatas[i].omega = od.omega[z:]

    return TrimSets(AccelDatas, RotaryDatas)



def FindSpike(_dataset):
    """ Only adjust the x & y axes
    TODO: smooth the data before finding the max magnitude?"""
    if type(_dataset) == AccelData:
        mag = np.sqrt(np.square(_dataset.getSingleAxis(0)) + np.square(_dataset.getSingleAxis(1)))

    elif type(_dataset) == RotaryData:
        mag = _dataset.omega

    else:
        raise ValueError('Unknown Dataset Type: ' + str(type(_dataset)))

    time_series = list(filter(lambda x: x < 7, list(_dataset.t)))
    # Here
    #  - 'lambda x: x < 7' = a function which returns the result of x < 7 for any x
    #      - this is the key in filter(key, arr) meaning that function will be applied to all elements in arr
    #  - filter( ) removes all values in an array that have returned false for the lambda expression
    #  - list( ) converts the object into an array

    abs_mag = np.absolute(mag[:len(time_series)])
    spike_t = time_series[np.argmax(abs_mag)]
    return spike_t


def TrimSets(ad_accel, ad_omega):
    """ Trims all data sets from SpikeAdjust to match the smallest one """
    min_dat = min_lambda(len, [
        min_lambda(len, ad_omega),
        min_lambda(len, ad_accel)
    ])

    for i in range(len(ad_accel)):
        ad_accel[i].a = np.array(
            [
                resample(ad_accel[i].getSingleAxis(0), len(min_dat.t)),
                resample(ad_accel[i].getSingleAxis(1), len(min_dat.t)),
                resample(ad_accel[i].getSingleAxis(2), len(min_dat.t))
            ]
        ).transpose()

        ad_accel[i].t = min_dat.t

    for i in range(len(ad_omega)):
        ad_omega[i].omega = np.array(resample(ad_omega[i].omega, len(min_dat.t)))
        ad_omega[i].t = min_dat.t

    return ad_accel, ad_omega
