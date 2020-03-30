import numpy as np
from sys import float_info


class Optimizer:
    def __init__(self, fn):
        self.fn = fn
        self.params = []
        self.configs = {}
        self.x = None
        self.grads = None
        self.limits = [-float_info.max, float_info.max]

    def FillParameters(self, *params):
        self.params = [*params]

    def config(self, *params):
        for i in params:
            self.configs[i[0]] = i[1]

    def Optimize(self, *params):
        return 'Ichi-byo Keika!'

    def SetLimits(self, _min=None, _max=None):
        self.limits = [
            _min if _min != None else self.limits[0],
            _max if _max != None else self.limits[1]
        ]

    def CallFunction(self, *values):
        return self.fn(*values, *self.params)

    def GradientApprox(self, x):
        try:
            self.configs['grad_approx']
        except KeyError:
            raise KeyError('Instance of Optimizer class does not contain the required config value: grad_approx')

        return (self.CallFunction(x + self.configs['grad_approx']) - self.CallFunction(
            x - self.configs['grad_approx'])) / (2 * self.configs['grad_approx'])


class AdamOptimizer_1D(Optimizer):
    def __init__(self, fn):
        Optimizer.__init__(self, fn)
        self.configs['N'] = 1000
        self.configs['x0'] = 0
        self.configs['grad_approx'] = 0.00001

    def Optimize(self, alpha, beta1, beta2, e=1e-8, return_array=False):
        m = [0] * self.configs['N']
        v = [0] * self.configs['N']
        x = [self.configs['x0']] * self.configs['N']

        grads = []

        for t in range(1, self.configs['N']):
            grad = self.GradientApprox(x[t - 1])
            grads.append(grad)
            m[t] = beta1 * m[t - 1] + (1 - beta1) * grad
            v[t] = beta2 * v[t - 1] + (1 - beta2) * pow(grad, 2)
            mc = m[t] / (1 - pow(beta1, t))
            vc = v[t] / (1 - pow(beta2, t))
            x[t] = x[t - 1] - alpha * mc / (np.sqrt(vc) + e)
            # The Following Code is problematic
            # Purpose: NaN Failsafe and looping limits
            if np.isnan(x[t]) or self.limits[0] < x[t] < self.limits[1]:
                if grad > 0:
                    x[t] = self.limits[1]
                elif grad < 0:
                    x[t] = self.limits[0]
                else:
                    x[t] = x[t-1]

        self.x = x
        self.grads = grads
        return x if return_array else x[-1]


class SGD_1D(Optimizer):
    def __init__(self, fn):
        Optimizer.__init__(self, fn)
        self.configs['N'] = 1000
        self.configs['x0'] = 0
        self.configs['grad_approx'] = 0.00001

    def Optimize(self, alpha, return_array=False):
        x = [self.configs['x0']] * self.configs['N']
        grads = []

        for t in range(self.configs['N'] - 1):
            grad = self.GradientApprox(x[t])
            grads.append(grad)
            x[t + 1] = x[t] - alpha * grad

        self.x = x
        self.grads = grads
        return x if return_array else x[-1]
