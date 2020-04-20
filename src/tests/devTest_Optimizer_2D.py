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
    return np.square(np.cos(theta)*r)


fn = cost_SimpleRotary

index = 30

parameters = {
    'a': acc_data.a[index],
    'a_next': acc_data.a[index + 1],
    'dt': acc_data.delta_t(index)
}



SGD = SGD_2D(fn)
# SGD.config(['x0', [xs[min_index], ys[min_index]]])
SGD.FillParameters(*list(parameters.values()))
x = SGD.Optimize(alpha=1e-4, return_array=False)
print('Result: \n Angle={0} \n Radius={1}'.format(-x[0], x[1]))
