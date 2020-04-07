from modules.Optimizers import *
import numpy as np
import matplotlib.pyplot as plt

fn = np.sin

Adam = AdamOptimizer_1D(fn)

x = Adam.Optimize(alpha=0.01, beta1=0.9, beta2=0.999, return_array=True)

it = 50
out = []
for i in range(len(x)):
    if i % it == 0:
        out.append(x[i])

if out[-1] != x[-1]:
    out.append(x[-1])

out = np.array(out)
time = np.arange(out[-1]-3, out[0]+3, 0.1) if out[-1] < out[0] else np.arange(out[0]-3, out[-1]+3, 0.1)

plt.plot(time, fn(time))
plt.plot(out, fn(out), 'o')
plt.show()