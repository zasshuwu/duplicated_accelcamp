
import numpy as np
import tensorflow as tf

##################################### tensorflow utilities

# simplification to run a session
# allows us to quickly build tests of low-level tf elements
# must be called AFTER creation of thigs like: param_phi = tf.Variable(1.0, name="phi")
def tfSessionInit():
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    return sess;

# simplify making a placeholder
def tfMakePlaceholder( aArray ):
    # tensorflow seems to dislike float64
    assert aArray.dtype == np.float32
    return tf.placeholder( aArray.dtype, aArray.shape )

########################################## parametrized functions

# functions from which we build our physics models
# the param_ variables are the ones that will be optimized
#******************

# rotate a 3-vector in the xy plane, i.e. rotation about the z-axis
# phi is in radians

def rot_xy(vec3, theta):
    # from https://stackoverflow.com/questions/37042748/how-to-create-a-rotation-matrix-in-tensorflow
    rot_matrix = [[tf.cos(theta), -tf.sin(theta),0],
                       [tf.sin(theta), tf.cos(theta),0],
                       [0.0,0.0,0.0]]

    # reshape to make tf.matmul happy ; no performance cost
    vec3 = tf.reshape(vec3, [3,1])

    return tf.matmul(rot_matrix, vec3)


def rot_2D(A, param_phi):
    # from https://stackoverflow.com/questions/37042748/how-to-create-a-rotation-matrix-in-tensorflow
    rotation_matrix = [[tf.cos(param_phi), -tf.sin(param_phi)],
                       [tf.sin(param_phi), tf.cos(param_phi)]]

    # to make tf.matmul happy
    A = tf.reshape(A, [2,1])
    return tf.matmul(rotation_matrix, A)


def curvatureBogus(A, param_r):
    # TODO : IMPLEMENT THIS
    return tf.reduce_sum(A * param_r)

# test degree of validity of the following hypothesis:
# A and Anext are 3-vecs in which we expect:
# [0] = tangential component
# [1] = radial componet
# [2] = perpendicular-to-plane component
# over the local time interval, and correspond to a radius of curvature param_r

def curvature(A, Anext, deltaT, param_r):
    # TODO : IMPLEMENT THIS
    ardot = ( Anext[1]-A[1] ) / deltaT
    term1 = param_r * tf.square(ardot)
    term2 = 4*A[1]*tf.square(A[0])
    return term1-term2



########################################## unit testing

def testrot2D( ):

    A = np.array([1.0, 0.0], np.float32)
    print("test_2D A shape", A.shape)
    ph_A = tfMakePlaceholder(A)

    param_phi = tf.Variable(1.0, name="phi")


    sess = tfSessionInit()

    func_rotate= rot_2D(ph_A, param_phi)
    print("fn_rot ", func_rotate)

    myFeed_dict = {ph_A: A}
    print("next line is sess.run")
    print( sess.run(func_rotate, feed_dict=myFeed_dict ))



def test_rot_xy():
    print("test_rot_xy")
    vec3 = np.array([1.0, 0.0, 0.0],np.float32)
    print("vec 3 shape ", vec3.shape)
    #tf_vec3 = tf.convert_to_tensor(vec3)
    ph_vec3 = tfMakePlaceholder(vec3)

    phi= tf.Variable(np.pi/2.0, tf.float32)
    print("call fn_rot")
    fn_rot = rot_xy(ph_vec3, phi)

    sess= tfSessionInit()
    print("next line sess run")
    output = sess.run(fn_rot, feed_dict={ph_vec3 : vec3})
    print( "fun result ", output)

# assert output
    out_expected = np.array([0.0, 1.0, 0.0],np.float32)
    tol = 0.1
    # assert abs(output[0]-out_expected[0])<tol

    #vec_out = rot_xy(vec1,phi)
    # assert( vec_out = [0,1,0])
    return 0

def runTests():
#    sess = tfSessionInit()
    testrot2D()
    test_rot_xy()


if __name__ == "__main__":
    runTests()

