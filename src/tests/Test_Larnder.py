
#----------------------
# various tests collected here, used as needed, mostly for dev purposes
#----------------------
from modules.tfPhysics import rot_xy
from modules.tfPhysics import rot_xy_noTF
import tensorflow as tf
from modules.PlotterIzk import *
from modules.DataStructures import *

from modules.Simulate import *
from modules.PlotterIzk import *
from modules.Cluster import *


def tfTest_CosineScalar():
    print("tfTest_CosineScalar")

    N = 1000
    phi = 0.5
    a = 1.0
    b = a * np.sin(phi)

    # ---
    # aVec3 =

    var_phi = tf.Variable(1.0, name='phi')

    ph_a = tf.placeholder(tf.float32, name='a')
    ph_b = tf.placeholder(tf.float32, name='b')

    init = tf.global_variables_initializer()

    cost = tf.square(b - a * tf.sin(var_phi))

    opt = tf.train.GradientDescentOptimizer(learning_rate=0.01)

    opt_out = opt.minimize(cost, var_list=[var_phi])

    with tf.Session() as sess:
        sess.run(init)

        sess.run(var_phi.assign(0.7))

        for i in range(1, N):
            feed_dict = {
                ph_a: a,
                ph_b: b,
            }
            _, loss, phi = sess.run([opt_out, cost, var_phi], feed_dict=feed_dict)
            print("Angle: {0}, Loss: {1}".format(phi, loss))


# ----------------------------------------------
def cost_noTF(a, b, phi):
    return 0


def cost_explicit(a, b, phi):
    return np.linalg.norm(b - rot_xy_noTF(a, phi))


def Test_TF_Optimize_RotXY():
    print("tfTest_CosineVec3")
    N = 30
    phi_true = 0.8
    phi_initial = 2.0

    # a and b are Vec3's
    a = np.array([0.0, 1.0, 0.0], np.float32)
    b = rot_xy_noTF(a, phi_true)  # tensorflow objects cant be in feed dict
    print("a ", a)
    print("b ", b)
    phi_true = 2.0
    explicitcost = cost_explicit(a, b, phi_true)
    print("ex cost", explicitcost)

    var_phi = tf.Variable(phi_initial, name='phi')

    ph_a = tf.placeholder(tf.float32, shape=(3,), name='a')
    ph_b = tf.placeholder(tf.float32, shape=(3,), name='b')

    init = tf.global_variables_initializer()

    #    cost = tf.reduce_sum(tf.square(b - rot_xy(a,var_phi)))
    cost = tf.norm(b - rot_xy(a, var_phi))
    # cost = rot_xy(a,var_phi)

    opt = tf.train.GradientDescentOptimizer(learning_rate=0.07)

    opt_out = opt.minimize(cost, var_list=[var_phi])
    outLoss = np.empty([N])
    outPhi = np.empty([N])

    with tf.Session() as sess:
        #sess.run(init)

        sess.run(var_phi.assign(phi_initial))

        for i in range(1, N):
            feed_dict = {ph_a: a, ph_b: b, }
            _, outLoss[i], outPhi[i] = sess.run([opt_out, cost, var_phi], feed_dict=feed_dict)
            print("Angle: {0}, Loss: {1}".format(outLoss[i], outPhi[i]))


# plot code: produces two figures, not sure why **************
    xAxis = np.arange(1,N,dtype=np.double)
    plotter = MultiPlotter(2,xAxis, "iteration #")
    plotter.setTitle("TensorFlow rotation test on a vec3")
    outLossTrim = outLoss[2:-1]  # skip the first value, it is always huge not sure why ******
    plotter.appendSignal(outLossTrim, 'loss', '')

    outPhiTrim = outPhi[2:-1]
    plotter.appendSignal(outPhiTrim, "phi (radians)", "phi value")
    plotter.display()

def test_Simulate():

    # simulation parameters
    deltaT = 0.1
    N = 100
    omega_0 = 100
    alphaFunction = AlphaSim_Sinusoidal1
    # alphaFunction = AlphaSim_S
    realRadius = 4

    rd = RotaryData_CreateFromAlphaFunction(alphaFunction, N, deltaT, omega_0)
    ad = AccelData_CreateFromRotary(rd, realRadius)

    mp = MultiPlotter( rd.t[:-2], 'Time')

    cost = mp.newSignal("cost")
    v = mp.newSignal("v")
    v2Predict = mp.newSignal("vnext predict")
    v2Data = mp.newSignal("vnext")

    for i in range(len(ad) - 1):
        cluster = Cluster_CreateFromAccelData(ad, i)


        cost.append(cluster.costDeltaV(realRadius))
        v.append(cluster.cell.v_UsingRadius(realRadius))
        v2Predict.append(cluster.cell.v_next_PredictedUsingRadius(realRadius))
        v2Data.append(cluster.v_next_UsingRadius(realRadius))

    mp.display()
    return

# ----------------------- main -----------------

# tfTest_CosineScalar()
#Test_TF_Optimize_RotXY()

test_Simulate()
