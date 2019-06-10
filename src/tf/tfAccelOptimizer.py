import numpy as np
import tensorflow as tf
from tfPhysics import *

class outputData:
    def __init__(self, length):
        self.rArray = np.ndarray(size=length)
        self.lossArray = np.ndarray(size=length)






class minimizer_curvature_noRot:

    def __init__(self, deltaT, nbIterations = 20 ):
        self.nbIterations = nbIterations
        vec3 = np.array(size=3, np.float32)

        self.ph_A = tfMakePlaceholder(vec3)
        self.ph_ANext = tfMakePlaceholder(vec3)
        self.deltaT=tf.constant(deltaT)
        self.param_r = tf.Variable(1.0, name="r")

        self.loss = curvature(self.ph_A, self.ph_ANext, self.deltaT, self.param_r)

        self.init = tf.global_variables_initializer()

        self.opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
        self.opt_op = opt.minimize(loss, var_list=[param_r] )

    def run(self, A, ANext):

        sess = tf.Session()
        sess.run(self.init)

        feed_dict = {self.ph_A: A, self.ph_ANext: ANext}
        for i in range(self.nbIterations):
            _, outputLoss, outr = sess.run([self.opt_op, self.loss, self.param_r],
                                              feed_dict=feed_dict)

        return r, loss



def main():

    #load ad
    #

    deltaT = ad.t[1] - ad.t[0]
    minner = minimizer_curvature_noRot(deltaT)

    output = outputArray( ad.len()-1)
    for i in range(ad.len()-1):
        A= np.array([ad.a[0][i],ad.a[1][i],ad.a[2][i]], np.float32)
        ANext = np.array([ad.a[0][i+1],ad.a[1][i+1],ad.a[2][i+1]], np.float32)
        output.r[i], output.loss[i] = minner.run(A,ANext)

# plot side by side: ar, at, r, loss

if __name__ == "__main__":
    main()












