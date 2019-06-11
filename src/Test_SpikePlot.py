from Load import *
from SpikeTracker import *
from Plotter import *
from scipy.signal import resample

run = LoadRun()

ad_accel = run["accel"]
ad_omega = run["omega"]

ad_accel, ad_omega = SpikeAdjust(ad_accel, ad_omega)

ad_accel[0].a = np.array(
    [
    resample(ad_accel[0].a[0], len(ad_omega[0].omega)),
    resample(ad_accel[0].a[1], len(ad_omega[0].omega)),
    resample(ad_accel[0].a[2], len(ad_omega[0].omega))
    ]
)
ad_accel[0].t = ad_omega[0].t
ad_accel.GenVec3()

Plot(ad_accel, ad_omega)
