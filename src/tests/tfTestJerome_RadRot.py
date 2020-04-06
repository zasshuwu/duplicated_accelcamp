import tensorflow as tf
from modules.Simulate import *
from modules.tfPhysics import cost_RadialRotation, rot_xy

# region Simulation
#config
alpha = 1
radius = 4
deltaT = 0.1
N = 500
omega_0 = 2
phi = 0.5

OmegaData = RotaryData_CreateFromAlphaFunction(alpha, N + 1, deltaT, omega_0)

a = AccelData_Rotate(AccelData_CreateFromRotary(OmegaData, radius), phi)
# endregion

# region TensorFlow Definitions
ph_a = tf.placeholder(shape=(3,), name='at', dtype=tf.float32)
ph_a_next = tf.placeholder(shape=(3,), name='ar_next', dtype=tf.float32)
ph_dt = tf.placeholder(name='dt', dtype=tf.float32)
var_r = tf.Variable(4.0, name='r', constraint=lambda x: tf.clip_by_value(x, 0.0, tf.float32.max), dtype=tf.float32)
var_phi = tf.Variable(.01, name='phi', dtype=tf.float32)

init = tf.global_variables_initializer()
# endregion

cost = tf.cond(
    rot_xy(ph_a, var_phi)[0] > 0,
    true_fn=lambda: cost_RadialRotation(ph_a, ph_a_next, ph_dt, var_r, var_phi),
    false_fn=lambda: tf.square(rot_xy(ph_a, var_phi)[0])*1e6
)

# cost = tf.nn.l2_loss(cost_RadialRotation(ph_a, ph_a_next, ph_dt, var_r, var_phi))

opt = tf.train.GradientDescentOptimizer(learning_rate=1e-3)
grads_and_vars = opt.compute_gradients(cost, var_list=[var_phi])
clipped_grads_and_vars = [(grad, var) for grad, var in grads_and_vars]
opt_out = opt.apply_gradients(clipped_grads_and_vars)

# opt_out = opt.minimize(cost, var_list=[var_phi])

with tf.Session() as sess:
    sess.run(init)

    for i in range(len(a)-1):
        feed_dict = {
            ph_a: a.a[i],
            ph_a_next: a.a[i + 1],
            ph_dt: a.t[i+1] - a.t[i]
        }

        _, loss, r, phi = sess.run([opt_out, cost, var_r, var_phi], feed_dict=feed_dict)
        print("{0}/{1} = Radius: {2}, Angle: {3}, Loss: {4}".format(i, len(a), r, phi, loss))
        # _, grad, loss, r, phi = sess.run([opt_out, grads_and_vars[0][0], cost, var_r, var_phi], feed_dict=feed_dict)
        # print("{0}/{1} = Radius: {2}, Angle: {3}, Loss: {4}, Grad: {5}".format(i, len(a), r, phi, loss, grad))

print("Radius found = {0}".format(r))
print("Angle found = {0}".format(phi))
