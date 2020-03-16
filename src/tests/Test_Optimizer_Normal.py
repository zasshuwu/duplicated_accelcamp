from modules.Optimizers import *
from modules.Simulate import *
import numpy as np
import matplotlib.pyplot as plt


def alphaFn(x):
    return 1


acc_data = AccelData_CreateFromRotary(RotaryData_CreateFromAlphaFunction(alphaFn, 52, 0.1), 4)


def cost_SimpleRadial(r, ar, ar_next, at, dt):
    ardot = r * (ar_next - ar) / dt
    term2 = np.square(at) * dt
    term3 = 2 * at * np.sqrt(ar * r)
    return np.square(ardot - term2 - term3)

fn = cost_SimpleRadial

index = 20

parameters = {
    'ar': acc_data.a[index][0],
    'ar_next': acc_data.a[index+1][0],
    'at': acc_data.a[index][1],
    'dt': acc_data.delta_t(index)
}

Adam = AdamOptimizer1D(cost_SimpleRadial)
Adam.config(['x0', 1])
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

plt.plot(time, fn(time, *list(parameters.values())))
plt.plot(out, fn(out, *list(parameters.values())), 'o')

i = 0.75
k = 0.2

for item in parameters:
    # This figtext value-bound string print method is exactly how print in python2.7 works
    plt.figtext(k, i, item + ": " + str("%.1f" % parameters[item]) + ";", color='red', fontsize="large")
    k += 0.250
    if k >= 0.55:
        k = 0.20
        i -= 0.15

plt.show()
