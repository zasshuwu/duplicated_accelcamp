from modules.Simulate import *
from modules.Plotter import *
from modules.Cluster import *
import tensorflow as tf
from modules.tfPhysics import cost_SimpleRadial


# simulation parameters
deltaT = 0.1
N = 100
omega_0 = 0.1
alphaFunction = AlphaSim_Sinusoidal1
#alphaFunction = AlphaSim_S
realRadius = 4

rotData = RotaryData_CreateFromAlphaFunction(alphaFunction, N, deltaT, omega_0 )
ad = AccelData_CreateFromRotary( rotData, realRadius )

# extra test
moreLoss = []
for i in range(len(ad) - 1):
    cluster = Cluster_CreateFromAccelData( ad, i)
    moreLoss.append( cluster.cost(realRadius))
# end extra test

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
newlosses = []

with tf.Session() as sess:
    sess.run(init)

    for i in range(len(ad)-1):
        ar= ad.getSingleAxis(0)[i]
        ar_next= ad.getSingleAxis(0)[i + 1]
        at = ad.getSingleAxis(1)[i]
        deltaT = ad.delta_t(i)

        feed_dict = {
            ph_ar: ar,
            ph_ar_next: ar_next,
            ph_at: at,
            ph_dt: deltaT
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

        # new computations
        cluster = Cluster_CreateFromAccelData(ad,i)
        newcost = cluster.cost2(realRadius)
        #newcost = cost_SimpleRadial(ar,ar_next,at,deltaT,realRadius)
        newlosses.append(newcost)


myPlotter = MultiPlotter(8, rotData.t[:-2], 'Time')
myPlotter.appendSignal(rotData.omega[:-2], 'Omega', '')
myPlotter.appendSignal(ad.getSingleAxis(0)[:-1], 'A_x', ad.model)
myPlotter.appendSignal(ad.getSingleAxis(1)[:-1], 'A_y', ad.model)
myPlotter.appendSignal(radii, 'Radius', '')
myPlotter.appendSignal(losses, 'Loss', '')
myPlotter.appendSignal(newlosses, 'newloss','')
myPlotter.appendSignal(moreLoss, 'moreLoss','')
myPlotter.display()
