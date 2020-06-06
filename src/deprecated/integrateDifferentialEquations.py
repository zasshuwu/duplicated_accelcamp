# load APMonitor package
#from apm import *

# Option 1: solve model with APM MATLAB
#z1 = apm_solve('2nd_order',4)

# Option 2: solve model with ODEINT
from scipy.integrate import odeint
import numpy as np

# x is the current state vector
# for a single-variable 2nd-order equation, it has dimension two
# return value is xdot, the derivative of x based on current state
# it also has dimension two

omega = 2
gamma = .2

def modelSHM(x,t):
  y = x[0]
  dy = x[1]
  K = 2
  gamma = .2
  xdot = [[], []]
  xdot[0] = dy
  xdot[1] = - K * y - gamma*dy
  return xdot

def modelSHMCoulomb(x,t):
  y = x[0]
  dy = x[1]
  K = 2
  F= .3
  gamma = .2
  xdot = [[], []]
  xdot[0] = dy
  xdot[1] = - K * y - gamma*dy - F*np.sign(dy)
  return xdot


def model(x,t):
  y = x[0]
  dy = x[1]  
  K = 30
  xdot = [[],[]]
  xdot[0] = dy
  xdot[1] = -(0.9+0.7*t)*dy - K * y
  return xdot

beginTime = 0
endTime =10
nSteps = 3000
time = np.linspace(beginTime,endTime,nSteps)
z2 = odeint(modelSHMCoulomb,[2,-1],time)
delta_t = (endTime-beginTime)/nSteps
accelShort = np.diff(z2[:,1])/delta_t
accel = np.append(accelShort,accelShort[-1])

# can try this version
#accelTest = np.ediff1d(z2[:,1], to_end=0.)
# or accel[:-1] = z[1:]-z[0:]


# plot results
import matplotlib.pyplot as plt
#plt.plot(z1['time'],z1['y'],'r-')
#plt.plot(z1['time'],z1['dy'],'b--')
plt.plot(time,z2[:,0],'r-')
#plt.plot(time,z2[:,1],'k-.')
plt.plot(time,accel,'g.')
plt.legend(['y (ODEINT)','accel'])
plt.xlabel('Time (s)')

plt.minorticks_on()
plt.grid(b=True, which='major', color='b', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.show()

# compare accel array with a parametrized functional form
ss