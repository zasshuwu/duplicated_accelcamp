
import numpy as np
import tensorflow as tf


def rotate(A, param_phi):
    A = tf.reshape(A, [2,1])
    # from https://stackoverflow.com/questions/37042748/how-to-create-a-rotation-matrix-in-tensorflow
    rotation_matrix = [[tf.cos(param_phi), -tf.sin(param_phi)],
                       [tf.sin(param_phi), tf.cos(param_phi)]]
    return tf.matmul(rotation_matrix, A)


def curvature(A, param_r):
    # TODO : IMPLEMENT THIS
    return tf.reduce_sum(A * param_r)

# def error(A,param_phi, param_r):
#     return curvature(rotate(A,param_phi),param_r)


def run():

    # TODO : Generate a sanity check that makes sense.
    A = np.random.rand(2)
    B = np.random.rand(2)
    C = np.random.rand(2)

    phi, r = infer_params(A, B, C)
    print("We got phi=%f and r=%f." % (phi, r))


def infer_params(A:np.ndarray, B:np.ndarray, C:np.ndarray):

    assert A.shape == (2,)
    assert B.shape == (2,)
    assert C.shape == (2,)

    ph_A = tf.placeholder(tf.float32, A.shape)
    ph_B = tf.placeholder(tf.float32, B.shape)
    ph_C = tf.placeholder(tf.float32, C.shape)

    param_phi = tf.Variable(0.0, name="phi")
    param_r = tf.Variable(1.0, name="r")

    kinetics_A = curvature(rotate(ph_A, param_phi), param_r)
    kinetics_B = curvature(rotate(ph_B, param_phi), param_r)
    kinetics_C = curvature(rotate(ph_C, param_phi), param_r)

    total_loss = tf.square(kinetics_A) + tf.square(kinetics_B) + tf.square(kinetics_C)

    init = tf.global_variables_initializer()

    # total_error = tf.sum([error(X, param_phi, param_r) for X in [ph_A, ph_B, ph_C]])

    opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
    # opt = tf.train.AdamOptimizer(learning_rate=0.01)
    # opt = tf.train.RMSPropOptimizer(learning_rate=0.1, decay=0.9, momentum=0.5)
    #
    opt_op = opt.minimize(total_loss, var_list=[param_phi, param_r])

    # your_gradients_woohoo = tf.gradient(total_loss, [param_phi, param_r])

    with tf.Session() as sess:

        sess.run(init)
        # load up some data

        feed_dict = {ph_A: A, ph_B:B, ph_C:C}
        for i in range(5):
            _, total_loss0, phi, r = sess.run([opt_op, total_loss, param_phi, param_r],
                                            feed_dict=feed_dict)
            print("The total loss was %f." % total_loss0)


        return phi, r
        # actual computation happens






if __name__ == "__main__":
    run()
