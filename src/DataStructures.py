import numpy as np

class AccelData:
    def __init__(self,a,t):
        self.a = a
        self.t = t
        self.len = len(self.a[0])
        self.GenVec3()

    def GenVec3(self):
        self.vec3 = []
        for i in range(len(self.a[0])):
            self.vec3.append(np.array([self.a[0][i], self.a[1][i], self.a[2][i]]))
        self.vec3 = np.array(self.vec3)

class RotaryData:
    def __init__(self,omega,t):
        self.omega = omega
        self.t = t
        self.len = len(self.omega)
