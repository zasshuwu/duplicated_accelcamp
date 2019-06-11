import numpy as np
import tensorflow as tf
from tfPhysics import *

import sys
if(sys.path.count('../') == 0):
    sys.path.append('../')
from Load import *
from Plotter import *
from DataStructures import *

#CONFIG
use_synthetic_data = True

class outputData:
    def __init__(self, length):
        self.r = np.empty(length)
        self.loss = np.empty(length)

class minimizer_curvature_noRot:

    def __init__(self, deltaT, nbIterations = 20 ):
        self.nbIterations = nbIterations
        vec3 = np.array([0,0,0], np.float32)

        self.ph_A = tfMakePlaceholder(vec3)
        self.ph_ANext = tfMakePlaceholder(vec3)
        self.deltaT=tf.constant(deltaT, np.float32)
        self.param_r = tf.Variable(1.0, name="r")

        self.loss = curvature(self.ph_A, self.ph_ANext, self.deltaT, self.param_r)

        self.init = tf.global_variables_initializer()

        self.opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
        self.opt_op = self.opt.minimize(self.loss, var_list=[self.param_r] )

    def run(self, A, ANext):

        sess = tf.Session()
        sess.run(self.init)

        feed_dict = {self.ph_A: A, self.ph_ANext: ANext}
        for i in range(self.nbIterations):
            _, outputLoss, outr = sess.run([self.opt_op, self.loss, self.param_r],
                                              feed_dict=feed_dict)

        return outr, outputLoss



def main():
    if(not use_synthetic_data):
        ad = LoadRun()["accel"][0]
        deltaT = ad.t[1] - ad.t[0]
    else:
        o = LoadRun()["omega"][0]
        radius = np.float32(input("PLEASE INPUT THE RADIUS:"))
        deltaT = o.t[1]-o.t[0]
        ar = []
        at = []
        az = []
        for i in range(o.len-1):
            ar.append(o.omega[i]**2+radius)
            at.append((o.omega[i+1] - o.omega[i]) / deltaT)
            az.append(0)
            print(i)
        ar = np.array(ar)
        at = np.array(at)
        az = np.array(az)
        a_temp = np.array([ar,at,az])
        ad = AccelData(a_temp, o.t)

    minner = minimizer_curvature_noRot(deltaT)
    length = ad.len - 1
    output = outputData( length)
    for i in range(length):
        A= ad.vec3[i]
        ANext = ad.vec3[i+1]
        output.r[i], output.loss[i] = minner.run(A,ANext)
        print(str(i)+"/"+str(ad.len) + " : " + str(output.r[i]))
    Curv_plot(ad.a[0][:length], ad.a[1][:length], output.r, output.loss, ad.t[:length])


if __name__ == "__main__":
    main()












