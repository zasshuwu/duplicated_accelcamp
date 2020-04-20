import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from modules.Optimizers import *
from modules.Simulate import *
from modules.Tools import rotate_vec3

# ========== Bullshit NaN Skip Explanation =============
# When Optimizing for the angle, there are a lot of big
# NaN zones and a lot of local minima. To resolve this,
# we iterate over a big grid of theta and radius values
# and calculate the cost for each value pair. Then, we
# find the global minimum on that grid while ignoring
# NaN values and we set the initial point to that location.
# This worked for the angle only but seems to not work when
# we optimize for both radius and angle. I am sorry...
# - Jerome C.
# =====================================================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def alphaFn(x):
    return 1


acc_data = AccelData_CreateFromRotary(
    RotaryData_CreateFromAlphaFunction(alphaFn, 52, 0.1),
    radius=4
)

acc_data = AccelData_Rotate(acc_data, 0)


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
    'a': acc_data.a[index],
    'a_next': acc_data.a[index + 1],
    'dt': acc_data.delta_t(index)
}

xtest = np.arange(-12, 12, 0.01)
ytest = np.arange(0, 120, 1)

xs = np.array([xtest]*len(ytest))
ys = np.array([ytest]*len(xtest)).transpose()

if xs.shape != ys.shape:
    raise ValueError('For some reason, xs.shape != ys.shape')

zs = np.empty([len(ytest), len(xtest)])

print('Bullshit NaN Skip Grid is : {0}x{1}'.format(len(ytest), len(xtest)))

if zs.shape != ys.shape:
    raise ValueError('For some reason, zs.shape != ys.shape')

for i in range(len(ytest)):
    for j in range(len(xtest)):
        zs[i, j] = fn(xs[i, j], ys[i, j], *parameters.values())

print('Bullshit NaN skip has been completed')
SGD = SGD_2D(fn)
min_index = np.unravel_index(np.nanargmin(zs), zs.shape)
print('Bullshit NaN skip start point: (theta={0}, r={1}) = {2}'.format(xs[min_index], ys[min_index], zs[min_index]))
SGD.config(['x0', [xs[min_index], ys[min_index]]])
SGD.FillParameters(*list(parameters.values()))
x = SGD.Optimize(alpha=1e-4, return_array=False)
print('Result: \n Angle={0} \n Radius={1}'.format(-x[0], x[1]))
