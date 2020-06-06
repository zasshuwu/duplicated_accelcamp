import matplotlib.pyplot as plt
from modules.Optimizers import *
from modules.Simulate import *
from modules.Tools import rotate_vec3


def alphaFn(x):
    return 1


def grad_approx(fn, x, qual, *params):
    return (
                   fn(x + qual, *params)
                   -
                   fn(x - qual, *params)
           ) / (2 * qual)


acc_data = AccelData_CreateFromRotary(
    RotaryData_CreateFromAlphaFunction(alphaFn, 52, 0.1),
    radius=4
)

acc_data = AccelData_Rotate(acc_data, 2)


def cost_SimpleRotary(theta, r, a, a_next, dt):
    a = rotate_vec3(a, theta)
    a_next = rotate_vec3(a_next, theta)
    ardot = (a_next[0] - a[0]) / dt
    term2 = np.square(a[1]) * dt / r  # traceback here
    term3 = 2 * a[1] * np.sqrt(a[0] / r)
    return np.square(ardot - term2 - term3)


fn = cost_SimpleRotary

index = 30

parameters = {
    'r': 4,
    'a': acc_data.a[index],
    'a_next': acc_data.a[index + 1],
    'dt': acc_data.delta_t(index)
}

time = np.arange(-2 * np.pi, 2 * np.pi, 0.001)
time_fn = np.array(fn(time, *list(parameters.values())))

tmin = np.nanmin(time_fn)
tmin_index = np.where(time_fn == tmin)[0][0]

Adam = AdamOptimizer_1D(fn)
Adam.config(['x0', time[tmin_index]])
Adam.FillParameters(*list(parameters.values()))
x = Adam.Optimize(alpha=0.01, beta1=0.9, beta2=0.999, return_array=True)

print('Result: ' + str(x[-1]))

it = 50
out = []
for i in range(len(x)):
    if i % it == 0:
        out.append(x[i])

if out[-1] != x[-1]:
    out.append(x[-1])

out = np.array(out)
# time = np.arange(out[-1] - 3, out[0] + 3, 0.001) if out[-1] < out[0] else np.arange(out[0] - 3, out[-1] + 3, 0.001)

plt.plot(time, fn(time, *list(parameters.values())), color='blue')
plt.plot(out, fn(out, *list(parameters.values())), 'o', color='green')
plt.plot(out[0], fn(out[0], *list(parameters.values())), 'o', color='black')
plt.annotate('Start', (out[0], fn(out[0], *list(parameters.values()))))

origins = out, fn(out, *list(parameters.values()))
gradients = -grad_approx(fn, out, 0.00001, *list(parameters.values()))*0.00001
plt.quiver(origins[0], origins[1], gradients, 0, color='purple', width=0.005)

i = 0.80
k = 0.65

for item in parameters:
    # This figtext value-bound string print method is exactly how print in python2.7 works
    # plt.figtext(k, i, item + ": " + str("%.1f" % parameters[item]) + ";", color='red', fontsize="large")
    i -= 0.05

# plt.ylim(-1, 500)
plt.ylabel('cost')
plt.xlabel('angle')
plt.show()
