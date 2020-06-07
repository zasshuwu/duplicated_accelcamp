
import numpy as np
import tensorflow as tf

##################################### tensorflow utilities

# placeholders: elements in a cost function that will be assigned values from
# data via dictionary assignments

# variables: elements in a cost function whose value will be determined by
# the minimization process. In the definition of a cost function, these elements
# typically written with the prefix "param_

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

    out = tf.matmul(rot_matrix, vec3)
    trans = tf.transpose(out)
    return trans[0]

def rot_xy_noTF(vec3, theta):
    # from https://stackoverflow.com/questions/37042748/how-to-create-a-rotation-matrix-in-tensorflow
    rot_matrix = [[np.cos(theta), -np.sin(theta),0],
                       [np.sin(theta), np.cos(theta),0],
                       [0.0,0.0,0.0]]

    # reshape to make tf.matmul happy ; no performance cost
   # vec3 = tf.reshape(vec3, [3,1])

    return np.matmul(rot_matrix, vec3)

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
    ardot = ( Anext[0]-A[0] ) / deltaT
    term1 = param_r * tf.square(ardot)
    term2 = 4*A[0]*tf.square(A[1])
    return term1-term2

def radiusAndAngleXY( A, Anext, deltaT, param_r, param_phi ):
    Aprime= rot_xy(A)
    AnextPrime = rot_xy(Anext)
    return curvature(Aprime, AnextPrime,deltaT,param_r)




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


def cost_SimpleAlpha(at, alpha, r):
    return tf.square(at-alpha*r)

def cost_SimpleRadial2(ar, ar_next, at, dt, r):
    ardot = (ar_next-ar)/dt
    term2 = tf.square(at)/r * dt
    term3 = 2 * at * tf.sqrt(ar/r)
    return tf.square(ardot - term2 - term3)


def cost_SimpleRadial(ar, ar_next, at, dt, r):
    ardot = r * (ar_next-ar)/dt
    term2 = tf.square(at) * dt
    term3 = 2 * at * tf.sqrt(ar*r)
    return tf.square(ardot - term2 - term3)


def cost_RadialRotation(a, a_next, dt, r, phi):
    a = rot_xy(a, phi)
    a_next = rot_xy(a_next, phi)
    ardot = r * (a_next[0]-a[0])/dt
    term2 = tf.square(a[1]) * dt
    term3 = 2 * a[1] * tf.sqrt((a[0])*r)
    return tf.square(ardot - term2 - term3)
