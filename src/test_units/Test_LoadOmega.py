from LoadOmega import *
from Plotter import *
from Simulate import *

radius = 10
phi = 0
omega = Load_Omega('..\\..\\data\\Dataset 2\\run2\\run2.omega.pasco.csv')
accel = convertOmegaAccel(omega, radius, phi)

Plot([accel], [omega])
