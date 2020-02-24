import sys
sys.path.append('../')
import tensorflow as tf
from modules.Simulate import *
from modules.tfPhysics import rot_xy

# region Simulation
#config
alpha = 1
radius = 4
deltaT = 0.1
N = 10
omega_0 = 2
phi = 0.01

OmegaData = simAlpha(N + 1, deltaT, alpha, omega_0, (0, 0.1))

a_not_rotated = convertOmegaAccel(OmegaData, radius)
a_rotated = convertOmegaAccel(OmegaData, radius, phi)
# endregion

# region TensorFlow Definitions
ph_a = tf.placeholder(tf.float32, shape=(3,), name='at')
ph_a_not = tf.placeholder(tf.float32, shape=(3,), name='ar_next')
var_phi = tf.Variable(2.0, name='phi')


init = tf.global_variables_initializer()
# endregion

cost = tf.square(tf.norm(rot_xy(ph_a, var_phi) - ph_a_not))

opt = tf.train.GradientDescentOptimizer(learning_rate=0.001)

opt_out = opt.minimize(cost, var_list=[var_phi])

with tf.Session() as sess:
    sess.run(init)

    sess.run(var_phi.assign(0.01))

    for i in range(len(a_not_rotated)-1):
        feed_dict = {
            ph_a: a_rotated.a[i],
            ph_a_not: a_not_rotated.a[i],
        }
        _, loss, phi = sess.run([opt_out, cost, var_phi], feed_dict=feed_dict)
        print("Angle: {0}, Loss: {1}".format(-phi, loss))

print("Angle found = {0}".format(-phi))
