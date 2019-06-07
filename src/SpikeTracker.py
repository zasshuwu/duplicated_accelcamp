import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from MyFunctions import *
from Load import *

adjust = 0.5

def SpikeAdjust(AccelDatas, RotaryDatas):
    ad = AccelDatas[0]
    od = RotaryDatas[0]

    a = ad.a  # a[0] is time
    time1 = ad.t

    time1 = list(filter(lambda x: x < 7, list(time1)))
    ax = a[0][:len(time1)]
    ay = a[1][:len(time1)]

    mag = np.sqrt(np.square(ax) + np.square(ay))

    abs_mag = np.absolute(mag)

    b = od.omega
    time2 = od.t
    time2 = list(filter(lambda x: x < 5, list(time2)))

    omega = b[:len(time2)]
    abs_omega = np.absolute(omega)

    t1 = time1[np.argmax(abs_mag)]
    t2 = time2[np.argmax(abs_omega)]
    delta = t2 - t1
    time2 = od.t
    time2 -= delta + adjust
    print(time2)
    z = len(list(filter(lambda x: x < 0, time2)))
    time2 = np.array(list(filter(lambda x: x >= 0, time2)))
    omega = b[z:]
    abs_omega = np.absolute(omega)
    temp_t = ad.t - adjust
    w = len(list(filter(lambda x: x < 0, temp_t)))
    time1 = list(filter(lambda x: 0 <= x <= time2[-1], temp_t))
    print(time1[-1])
    ax = a[0][w:len(time1)+w]
    ay = a[1][w:len(time1)+w]
    return [AccelData([ax,ay,ad.a[2]],time1,ad.samplerate)],[RotaryData(omega,time2,od.samplerate)]
