class AccelData:
    def __init__(self,a,t,sr):
        self.a = a
        self.t = t
        self.samplerate = sr

    def len(self):
        return len(self.a[0])

class RotaryData:
    def __init__(self,omega,t,sr):
        self.omega = omega
        self.t = t
        self.samplerate = sr
