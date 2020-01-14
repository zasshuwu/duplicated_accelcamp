from Load import *
from SpikeTracker import *
from Plotter import *
from scipy.signal import resample
from MyFunctions import min_lambda

from unittest import *

# test via manual selection of data source ( explicit run of this file alone )
if __name__ == "__main__":
    run = LoadRun()
    ad_accel = run["accel"]
    ad_omega = run["omega"]

# for automated testing via test_main.py
else:
    dataDir = "../data/2019 06 12/0 degrees/run1/"
    ad_accel = [LoadAccelFile(dataDir+"run1.accel.x2.CSV")]
    ad_omega = [Load_Omega(dataDir+"run1.omega.pasco.csv")]


ad_accel, ad_omega = SpikeAdjust(ad_accel, ad_omega)

min_dat = min_lambda(len, [
    min_lambda(len, ad_omega),
    min_lambda(len, ad_accel)
])

for i in range(len(ad_accel)):
    ad_accel[i].a = np.array(
        [
        resample(ad_accel[i].a[0], len(min_dat.t)),
        resample(ad_accel[i].a[1], len(min_dat.t)),
        resample(ad_accel[i].a[2], len(min_dat.t))
        ]
    )
    ad_accel[i].t = min_dat.t

for i in range(len(ad_omega)):
    ad_omega[i].omega = np.array(resample(ad_omega[i].omega, len(min_dat.t)))
    ad_omega[i].t = min_dat.t

Plot(ad_accel, ad_omega)
