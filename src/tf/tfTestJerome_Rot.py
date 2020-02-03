import tensorflow as tf
from Simulate import *
from Load import *
from tf.tfPhysics import cost_RadialRotation

# region Simulation
#config
alpha = 1
radius = 4
deltaT = 0.1
N = 100
omega_0 = 2
phi = 0

OmegaData = simConstAlpha(N+1, deltaT, alpha, omega_0)

a = convertOmegaAccel(OmegaData, radius, phi)  # if input('use synthetic data (y/n):') == 'y' else LoadRun()['accel'][0]
# endregion

# region TensorFlow Definitions
ph_a = tf.placeholder(tf.float32, shape=(3,), name='at')
ph_a_next = tf.placeholder(tf.float32, shape=(3,), name='ar_next')
ph_dt = tf.placeholder(tf.float32, name='dt')
var_r = tf.Variable(4.0, name='r', constraint=lambda x: tf.clip_by_value(x, 0.0, tf.float32.max))
var_phi = tf.Variable(2.0, name='phi')

init = tf.global_variables_initializer()
# endregion

cost = cost_RadialRotation(ph_a, ph_a_next, ph_dt, var_r, var_phi)

opt = tf.train.GradientDescentOptimizer(learning_rate=0.001)

opt_out = opt.minimize(cost, var_list=[var_phi])

with tf.Session() as sess:
    sess.run(init)

    for i in range(len(a)-1):
        feed_dict = {
            ph_a: a.a[i],
            ph_a_next: a.a[i + 1],
            ph_dt: a.t[i+1] - a.t[i]
        }
        _, loss, r, phi = sess.run([opt_out, cost, var_r, var_phi], feed_dict=feed_dict)
        print("{0}/{1} = Radius: {2}, Angle: {3}, Loss: {4}".format(i, len(a), r, phi, loss[0]))

print("Radius found = {0}".format(r))
print("Angle found = {0}".format(phi))



