import tensorflow as tf
from modules.Simulate import *
from modules.Load import *
from tests.tfPhysics import cost_SimpleRadial
from modules.Plotter import *

# region Simulation
#config
alpha = 1
radius = 4
deltaT = 0.1
N = 20
omega_0 = 5

#OmegaData = simAlpha(N, deltaT, alpha, omega_0)
OmegaData = Load_Omega('C:\\Users\\Jerome\\Documents\\GitHub\\2019_06_AccelerationCamp\\data\\Dataset 1\\run2\\run2.omega.pasco.csv')

a = convertOmegaAccel(OmegaData, radius) #if input('use synthetic data (y/n): ') == 'y' else LoadRun()['accel'][0]
# endregion

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

myPlotter = MultiPlotter(5, OmegaData.t[:-2])
myPlotter.appendSignal(OmegaData.omega[:-2], 'Omega', 'From Sensor')
myPlotter.appendSignal(a.getSingleAxis(0)[:-1], 'A_x', a.model)
myPlotter.appendSignal(a.getSingleAxis(1)[:-1], 'A_y', a.model)
myPlotter.appendSignal(radii, 'Radius', '')
myPlotter.appendSignal(losses, 'Loss', '')
myPlotter.display()
