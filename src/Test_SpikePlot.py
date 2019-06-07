from Load import *
from SpikeTracker import *
from Plotter import *
from scipy.signal import resample

run = LoadRun()
ad_accel, ad_omega = SpikeAdjust(run["accel"],run["omega"])
'''
accels_len = []
for i in range(len(ad_accel)):
    accels_len.append({i:len(ad_accel[i].a[0])})

min_len = min(accels_len, key=accels_len.get)

omega_len = []
for i in range(len(ad_accel)):
    accels_len.append({i:len(ad_accel[i].a[0])})

min_len = min(accels_len, key=accels_len.get)'''

ad_accel[0].a[0] = resample(ad_accel[0].a[0], len(ad_omega[0].omega))
ad_accel[0].a[1] = resample(ad_accel[0].a[1], len(ad_omega[0].omega))
ad_accel[0].a[2] = resample(ad_accel[0].a[2], len(ad_omega[0].omega))
ad_accel[0].t = resample(ad_accel[0].t, len(ad_omega[0].t))

Plot(ad_accel,ad_omega)
