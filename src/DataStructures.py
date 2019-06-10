class AccelData:
    def __init__(self,a,t,sr):
        self.a = a
        self.t = t
        self.samplerate = sr
        self.len = len(self.a[0])

class RotaryData:
    def __init__(self,omega,t,sr):
        self.omega = omega
        self.t = t
        self.samplerate = sr
