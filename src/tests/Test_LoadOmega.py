from modules.LoadOmega import *
from modules.Plotter import *
from modules.Simulate import *

radius = 10
phi = 0
omega = Load_Omega('../../data/Dataset 2/run2/run2.omega.pasco.csv')
accel = AccelData_CreateFromRotary(omega, radius, phi)

Plot([accel], [omega])
