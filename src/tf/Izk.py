import sys
sys.path.append('../')
import tensorflow as tf
import numpy as np

N = 100
phi = 0.5
a = 1.0
b = a*np.sin(phi)

var_phi = tf.Variable(phi, name='phi')

ph_a = tf.placeholder(tf.float32, name='a')
ph_b = tf.placeholder(tf.float32, name='b')

init = tf.global_variables_initializer()

cost = tf.square(a - b*tf.sin(var_phi))

opt = tf.train.GradientDescentOptimizer(learning_rate=0.001)

opt_out = opt.minimize(cost, var_list=[var_phi])

with tf.Session() as sess:
    sess.run(init)

    sess.run(var_phi.assign(0.01))

    for i in range(1,10):
        feed_dict = {
            ph_a: a,
            ph_b: b,
        }
        _, loss, phi = sess.run([opt_out, cost, var_phi],feed_dict=feed_dict )
        print("Angle: {0}, Loss: {1}".format(phi, loss))

print("Angle found = {0}".format(phi))
