import matplotlib.pyplot as plt
import numpy as np
from modules.Optimizers import *
from modules.Simulate import *

def alphaFn(x):
    return (3 if x > 1 else 4) if x < 5 else 0


def grad_approx(fn, x, qual, *params):
    return (
                   fn(x + qual, *params)
                   -
                   fn(x - qual, *params)
           ) / (2 * qual)


acc_data = AccelData_CreateFromRotary(RotaryData_CreateFromAlphaFunction(alphaFn, 52, 0.1), 4)


def cost_SimpleRadial(r, ar, ar_next, at, dt):
    ardot = (ar_next - ar) / dt
    term2 = np.square(at) * dt / r
    term3 = 2 * at * np.sqrt(ar / r)
    return np.square(ardot - term2 - term3)


fn = cost_SimpleRadial

Adam = AdamOptimizer_1D(cost_SimpleRadial)
Adam.config(['x0', 2])

x = []
it = 10

time = np.arange(-0.1, 10.1, 0.1)
for index in range(len(acc_data)-1):
    out = []
    parameters = {
        'ar': acc_data.a[index][0],
        'ar_next': acc_data.a[index + 1][0],
        'at': acc_data.a[index][1],
        'dt': acc_data.delta_t(index)
    }
    Adam.FillParameters(*list(parameters.values()))
    x = Adam.Optimize(alpha=0.01, beta1=0.9, beta2=0.999, return_array=True)

    for i in range(len(x)):
        if i % it == 0:
            out.append(x[i])

    if out[-1] != x[-1]:
        out.append(x[-1])

    out = np.array(out)
    if index % it == 0:
        plt.plot(out, fn(out, *list(parameters.values())), 'o')
        plt.plot(time, fn(time, *list(parameters.values())))

plt.ylim(-1, 100)
plt.ylabel('cost')
plt.xlabel('radius')
plt.show()
