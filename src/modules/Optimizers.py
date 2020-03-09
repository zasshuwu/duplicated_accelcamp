import numpy as np


class Optimizer:
    def __init__(self, fn):
        self.fn = fn
        self.params = []
        self.configs = {}

    def FillParameters(self, *params):
        self.params = [*params]

    def config(self, *params):
        for i in params:
            self.configs[i[0]] = i[1]

    def Optimize(self, *params):
        return 'Ichi-byo Keika!'


class AdamOptimizer1D(Optimizer):
    def __init__(self, fn):
        Optimizer.__init__(self, fn)
        self.configs['N'] = 1000
        self.configs['x0'] = 0


    def Optimize(self, alpha, beta1, beta2, e=1e-8):
        m = [0]*self.configs['N']
        v = [0]*self.configs['N']
        x = [self.configs['x0']]*self.configs['N']

        for i in range(self.configs['N']):



