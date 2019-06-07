
import numpy as np
import tensorflow as tf

# simplification to run a session
# allows us to quickly build tests of low-level tf elements
def tfSessionInit():
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    return sess;

# expects a numpy array
def tfMakePlaceholderFor( aArray ):
    return tf.placeholder( aArray.dtype, aArray.shape )


# functions from which we build our physics models
# the param_ variables are the ones that will be optimized
#******************

# rotate a 3-vector in the xy plane, i.e. rotation about the z-axis
# phi is in radians

def rot_xy(aVec3, param_phi):
    # from https://stackoverflow.com/questions/37042748/how-to-create-a-rotation-matrix-in-tensorflow
    rotation_matrix = [[tf.cos(param_phi), -tf.sin(param_phi),0],
                       [tf.sin(param_phi), tf.cos(param_phi),0],
                       [0.0,0.0,0.0]]

    # reshape to make tf.matmul happy
    aVec3 = tf.reshape(aVec3, [3,1])

    return tf.matmul(rotation_matrix, aVec3)



def test_rot_xy( aSession ):
    print("test_rot_xy")
    vec1 = tf.Variable([1,0,0],tf.float32)

    ph_A = tf.placeholder(tf.float32, A.shape)
    # this should be 90 degrees, in radians
    # calc that value..tf.
    phi= tf.Variable([.5], tf.float32)

    aSession.run(z, feed_dict={x: [[3.0, 4.0], [5.0, 6.0]]})

    C = np.random.rand(3)

    vec_out = rot_xy(vec1,phi)
    # assert( vec_out = [0,1,0])
    return 0

# test degree of validity of the following hypothesis:
# 3-vectors A and Anext are in the approrpiate radial-tangential coordinates
# over the local time interval, and correspond to a radius of curvature param_r

def curvature(A, param_r):
    # TODO : IMPLEMENT THIS
    return tf.reduce_sum(A * param_r)


def runTests():
    sess = tfSessionInit()
    test_rot_xy(sess)


if __name__ == "__main__":
    runTests()
