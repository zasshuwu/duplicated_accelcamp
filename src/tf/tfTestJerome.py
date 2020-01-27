import tensorflow as tf
from Simulate import *
from Load import *
from tf.tfPhysics import cost_SimpleAlpha, cost_SimpleRadial

# def cost_SimpleRadial()
# def cost_RadialAndRotate( angle)
#     rot_xy(a,angle)
#     return cost_SimpleRadial()


#config
alpha = 1
radius = 4
deltaT = 0.1
N = 20
omega_0 = 5

OmegaData = simConstAlpha(N, deltaT, alpha, omega_0)

a = convertOmegaAccel(OmegaData, radius) if input('use synthetic data (y/n): ') == 'y' else LoadRun()['accel'][0]

# for r in range(1,8):
#     print('r ', r, 'loss ', cost_SimpleRadial2(a.a[0][1], a.a[1][0],a,a[0][1],deltaT))

# tf stuff

ph_at = tf.placeholder(tf.float32, name='at')
ph_ar = tf.placeholder(tf.float32, name='ar')
ph_ar_next = tf.placeholder(tf.float32, name='ar_next')
ph_dt = tf.placeholder(tf.float32, name='dt')
var_r = tf.Variable(1.0, name='r')
#alpha = tf.constant(alpha, tf.float32)

init = tf.global_variables_initializer()

#cost = cost_SimpleAlpha(ph_at, alpha, var_r)
cost = cost_SimpleRadial(ph_ar, ph_ar_next, ph_at, ph_dt, var_r)

opt = tf.train.GradientDescentOptimizer(learning_rate=0.001)
# opt = tf.train.AdamOptimizer(learning_rate=0.01)
# opt = tf.train.RMSPropOptimizer(learning_rate=0.1, decay=0.9, momentum=0.5)

opt_out = opt.minimize(cost, var_list=[var_r])

with tf.Session() as sess:
    sess.run(init)

    for i in range(len(a)-1):
        feed_dict = {
            ph_ar: a.getSingleAxis(0)[i],
            ph_ar_next: a.getSingleAxis(0)[i + 1],
            ph_at: a.getSingleAxis(1)[i],
            ph_dt: a.t[i+1] - a.t[i]
        }
        _, loss, r = sess.run([opt_out, cost, var_r], feed_dict=feed_dict)
        print(str(i)+"/"+str(len(a)) + " = Radius: " + str(r)+", Loss: " + str(loss))

print("Radius found = {0}".format(r))



