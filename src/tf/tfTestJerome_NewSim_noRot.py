from Simulate import *
from Plotter import *
import tensorflow as tf
from tfPhysics import cost_SimpleRadial

activate_console_menu = True
# region Console Menu Config
alphaFunction = 10.0
function_dict = {
    'a': AlphaSim_Piecewise1,
    'b': AlphaSim_Piecewise2,
    'c': AlphaSim_Sinusoidal1
}

if activate_console_menu:
    print('=====Choose an Option=====')
    for i in function_dict.keys():
        print("{0}: {1}".format(i, function_dict[i]))

    print(chr(97+len(function_dict)) + ': Choose a Constant Value')

    choice = input('Write the Letter: ')

    if choice == chr(98+len(function_dict)):
        raise NotImplementedError('This is not a valid selection.')

    elif choice == chr(97+len(function_dict)):
        alphaFunction = float(input('Choose a value: '))

    else:
        alphaFunction = function_dict[choice]
# endregion

# region Simulation
deltaT = 0.1
N = 100
omega_0 = 0.1
omega_noise = (0, 0)

radiusFunction = 4
accel_noise = (0, 0)

OmegaData = simAlpha(N, deltaT, alphaFunction, omega_0, noise=(0, 0))

a = convertOmegaAccel(OmegaData, radiusFunction, noise=accel_noise)
# endregion

alphaArray = AlphaSim_GenerateAlphaArray(alphaFunction, N, deltaT)

# region TensorFlow Definitions
ph_at = tf.placeholder(tf.float32, name='at')
ph_ar = tf.placeholder(tf.float32, name='ar')
ph_ar_next = tf.placeholder(tf.float32, name='ar_next')
ph_dt = tf.placeholder(tf.float32, name='dt')
var_r = tf.Variable(1.0, name='r')

init = tf.global_variables_initializer()
# endregion

cost = cost_SimpleRadial(ph_ar, ph_ar_next, ph_at, ph_dt, var_r)

opt = tf.train.GradientDescentOptimizer(learning_rate=0.001)

opt_out = opt.minimize(cost, var_list=[var_r])


radii = []
losses = []
with tf.Session() as sess:
    sess.run(init)

    for i in range(len(a)-1):
        feed_dict = {
            ph_ar: a.getSingleAxis(0)[i],
            ph_ar_next: a.getSingleAxis(0)[i + 1],
            ph_at: a.getSingleAxis(1)[i],
            ph_dt: a.t[i+1] - a.t[i]
        }
        sess.run(var_r.assign(1))
        for j in range(10):
            sess.run(opt_out, feed_dict=feed_dict)
        r, loss = sess.run([var_r, cost], feed_dict=feed_dict)
        # print("{2}/{3} = Radius: {0}, Loss: {1}".format(
        #     r, loss, i, len(a)-1
        # ))
        radii.append(r)
        losses.append(loss)

myPlotter = MultiPlotter(6, OmegaData.t[:-2], 'Time')
myPlotter.appendSignal(alphaArray[:-2], 'Alpha', '')
myPlotter.appendSignal(OmegaData.omega[:-2], 'Omega', '')
myPlotter.appendSignal(a.getSingleAxis(0)[:-1], 'A_x', a.model)
myPlotter.appendSignal(a.getSingleAxis(1)[:-1], 'A_y', a.model)
myPlotter.appendSignal(radii, 'Radius', '')
myPlotter.appendSignal(losses, 'Loss', '')
myPlotter.display()
