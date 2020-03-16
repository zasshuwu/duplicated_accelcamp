import numpy as np


class Optimizer:
    def __init__(self, fn):
        self.fn = fn
        self.params = []
        self.configs = {}
        self.x = None

    def FillParameters(self, *params):
        self.params = [*params]

    def config(self, *params):
        for i in params:
            self.configs[i[0]] = i[1]

    def Optimize(self, *params):
        return 'Ichi-byo Keika!'

    def CallFunction(self, *values):
        return self.fn(*values, *self.params)


class AdamOptimizer1D(Optimizer):
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
            grad = (
                           self.CallFunction(x[t - 1] + self.configs['grad_approx'])
                           -
                           self.CallFunction(x[t - 1] - self.configs['grad_approx'])
                   ) / (2 * self.configs['grad_approx'])
            grads.append(grad)
            m[t] = beta1 * m[t - 1] + (1 - beta1) * grad
            v[t] = beta2 * v[t - 1] + (1 - beta2) * pow(grad, 2)
            mc = m[t] / (1 - pow(beta1, t))
            vc = v[t] / (1 - pow(beta2, t))
            x[t] = x[t - 1] - alpha * mc / (np.sqrt(vc) + e)

        self.x = x
        return x[:-1] if return_array else x
