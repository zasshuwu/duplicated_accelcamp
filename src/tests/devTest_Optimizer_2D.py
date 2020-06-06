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


def cost_SimpleRotary(theta, r):
    return np.square(np.cos(theta)*np.cos(r))


fn = cost_SimpleRotary

xtest = np.arange(-5, 5, 0.1)
ytest = np.arange(-5, 5, 0.1)

xs = np.array([xtest]*len(ytest))
ys = np.array([ytest]*len(xtest)).transpose()
zs = np.empty([len(xtest), len(ytest)])

for i in range(len(xtest)):
    for j in range(len(ytest)):
        zs[i, j] = fn(xs[i, j], ys[i, j])

ax.scatter(xs, ys, zs)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

SGD = SGD_2D(fn)
x = SGD.Optimize(alpha=1e-4, return_array=False)
print('Result: \n Angle={0} \n Radius={1}'.format(-x[0], x[1]))

plt.show()
