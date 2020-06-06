from modules.Load import *
from modules.SpikeTracker import *
from modules.Plotter import *

# test via manual selection of data source ( explicit run of this file alone )
if __name__ == "__main__":
    run = LoadMultiRun()
    ad_accel = run["accel"]
    ad_omega = run["omega"]

# for automated testing via test_main.py
else:
    dataDir = "../../data/2019 06 12/0 degrees/run1/"
    ad_accel = [LoadAccelFile(dataDir+"run1.accel.x2.CSV")]
    ad_omega = [Load_Omega(dataDir+"run1.omega.pasco.csv")]


ad_accel, ad_omega = SpikeAdjust(ad_accel, ad_omega)

Plot(ad_accel, ad_omega)
