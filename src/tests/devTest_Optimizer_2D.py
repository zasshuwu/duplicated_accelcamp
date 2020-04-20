import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from modules.Optimizers import *
from modules.Simulate import *
from modules.Tools import rotate_vec3

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
ytest = np.arange(-12, 12, 0.01)

xs = np.array([xtest]*len(ytest))
ys = np.array([ytest]*len(xtest)).transpose()
zs = np.empty([len(xtest), len(ytest)])

for i in range(len(xtest)):
    for j in range(len(ytest)):
        zs[i, j] = fn(xs[i, j], ys[i, j], *parameters.values())

ax.scatter(xs, ys, zs)
ax.set_zlim3d(0, 500)
ax.set_xlabel('Angle, theta')
ax.set_ylabel('Radius, r')
ax.set_zlabel('Cost')
plt.show()
