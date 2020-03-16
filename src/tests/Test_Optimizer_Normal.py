import matplotlib.pyplot as plt
import numpy as np
from modules.Optimizers import *
from modules.Simulate import *


def alphaFn(x):
    return 1


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

index = 20

parameters = {
    'ar': acc_data.a[index][0],
    'ar_next': acc_data.a[index + 1][0],
    'at': acc_data.a[index][1],
    'dt': acc_data.delta_t(index)
}

Adam = AdamOptimizer1D(cost_SimpleRadial)
Adam.config(['x0', 2])
Adam.FillParameters(*list(parameters.values()))
x = Adam.Optimize(alpha=0.01, beta1=0.9, beta2=0.999, return_array=True)

it = 50
out = []
for i in range(len(x)):
    if i % it == 0:
        out.append(x[i])

if out[-1] != x[-1]:
    out.append(x[-1])

out = np.array(out)
time = np.arange(out[-1] - 3, out[0] + 3, 0.1) if out[-1] < out[0] else np.arange(out[0] - 3, out[-1] + 3, 0.1)

plt.plot(time, fn(time, *list(parameters.values())), color='blue')
plt.plot(out, fn(out, *list(parameters.values())), 'o', color='green')
plt.plot(out[0], fn(out[0], *list(parameters.values())), 'o', color='black')
plt.annotate('Start', (out[0], fn(out[0], *list(parameters.values()))))

origins = out, fn(out, *list(parameters.values()))
gradients = -grad_approx(fn, out, 0.00001, *list(parameters.values()))*0.00001
plt.quiver(*origins, gradients, 0, color='purple', width=0.005)

i = 0.80
k = 0.65

for item in parameters:
    # This figtext value-bound string print method is exactly how print in python2.7 works
    plt.figtext(k, i, item + ": " + str("%.1f" % parameters[item]) + ";", color='red', fontsize="large")
    i -= 0.05

plt.ylim(-1, 100)
plt.ylabel('cost')
plt.xlabel('radius')
plt.show()
