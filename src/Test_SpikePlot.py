from Load import *
from SpikeTracker import *
from Plotter import *

run = LoadRun()
ad_accel, ad_omega = SpikeAdjust(run["accel"],run["omega"])
Plot(ad_accel,ad_omega)
