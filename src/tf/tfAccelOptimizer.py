import numpy as np
import tensorflow as tf
from tfPhysics import *

import sys
if(sys.path.count('../') == 0):
    sys.path.append('../')
from Load import *
from Plotter import *
from DataStructuresNew import *
from Simulate import *

#CONFIG
use_synthetic_data = True if input("use synthetic data? (y/n): ") == "y" else False
if use_synthetic_data:
    use_omega_file = True if input("use omega file? (y/n): ") == "y" else False

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
        self.opt_op = self.opt.minimize(self.loss, var_list=[self.param_r])

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
    else:
        if(use_omega_file):
            o = LoadRun()["omega"][0]
        else:
            o = simConstAlpha(
                int(input("Number of iterations: ")),
                np.float32(input("Delta t: ")),
                np.float32(input("alpha: ")),
                np.float32(input("omega at t=0: "))
            )
        ad = convertOmegaAccel(o, np.float32(input("Radius: ")))
    deltaT = ad.t[1] - ad.t[0]
    minner = minimizer_curvature_noRot(deltaT)
    length = len(ad) - 1
    output = outputData(length)
    for i in range(length):
        A= ad.a[i]
        ANext = ad.a[i+1]
        output.r[i], output.loss[i] = minner.run(A, ANext)
        print(str(i)+"/"+str(len(ad)) + " = Radius: " + str(output.r[i])+", Loss: " + str(output.loss[i]))
    Curv_plot(ad.getSingleAxis(0)[:length],ad.getSingleAxis(1)[:length],output.r, output.loss, ad.t[:length])


if __name__ == "__main__":
    main()












