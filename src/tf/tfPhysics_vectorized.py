
import numpy as np
import tensorflow as tf


def rotate(A:tf.Tensor, param_phi):
    # from https://stackoverflow.com/questions/37042748/how-to-create-a-rotation-matrix-in-tensorflow
    rotation_matrix = [[tf.cos(param_phi), -tf.sin(param_phi), 0.0],
                       [tf.sin(param_phi), tf.cos(param_phi), 0.0],
                       [0.0, 0.0, 0.0]]
    return tf.transpose(tf.matmul(rotation_matrix, tf.transpose(A)))


def curvature(A, param_r):
    # this returns a tensor of shape (window_size,)
    return tf.reduce_sum(A * param_r, axis=1)



# def error(A,param_phi, param_r):
#     return curvature(rotate(A,param_phi),param_r)


def run():
    window_size = 5
    A = np.random.rand(window_size, 3)
    phi, r = infer_params(A)
    print("We got phi=%f and r=%f." % (phi, r))


def infer_params(A:np.ndarray):

    assert A.shape[1] == 3
    ph_A = tf.placeholder(tf.float32, A.shape)

    param_phi = tf.Variable(0.0, name="phi")
    param_r = tf.Variable(1.0, name="r")

    kinetics_A = curvature(rotate(ph_A, param_phi), param_r)
    total_loss = tf.reduce_mean(tf.square(kinetics_A))

    # total_error = tf.sum([error(X, param_phi, param_r) for X in [ph_A, ph_B, ph_C]])

    #optim = tf.train.GradientDescentOptimizer(learning_rate=0.1)
    optim = tf.train.AdamOptimizer(learning_rate=0.01)
    # optim = tf.train.RMSPropOptimizer(learning_rate=0.1, decay=0.9, momentum=0.5)
    #
    optim_op = optim.minimize(total_loss, var_list=[param_phi, param_r])

    # your_gradients_woohoo = tf.gradient(total_loss, [param_phi, param_r])

    # print("Global variables are :")
    # print([str(i.name) for i in tf.global_variables()])
    # print("Local variables are :")
    # print([str(i.name) for i in tf.local_variables()])

    init_op = tf.global_variables_initializer()
    with tf.Session() as sess:

        sess.run(init_op)
        # load up some data

        feed_dict = {ph_A: A}
        for i in range(50):
            # sess.run(optim_op, feed_dict=feed_dict)
            _, total_loss0 = sess.run([optim_op, total_loss], feed_dict=feed_dict)
            #total_loss0, phi, r = sess.run([total_loss, param_phi, param_r],
            #                                feed_dict=feed_dict)

            print("The total loss was %f." % total_loss0)

        phi, r = sess.run([param_phi, param_r])
        return phi, r
        # actual computation happens






if __name__ == "__main__":
    run()
