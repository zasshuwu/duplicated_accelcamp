import unittest
import numpy as np
import tensorflow as tf

# (Guillaume) This doesn't want to cooperate, and I'm not sure about the easiest way to resolve this.
# One option would be to include things in the PYTHONPATH environment variable,
# but it would be a messy solution. Hmmm ...
#
# from tfPhysics import tfSessionInitRun


class TestTensorflowOperations(unittest.TestCase):

    def test_adding_vectors(self):
        vec3 = np.array([1.0,0.0,0.0])
        reference_value = vec3 + vec3

        ph_vec3 = tf.placeholder(tf.float32, vec3.shape)
        my_sum = ph_vec3 + ph_vec3
        my_feed_dict = {ph_vec3: vec3}

        sess = tf.Session() # tfSessionInitRun()
        experimental_value = sess.run(my_sum, feed_dict=my_feed_dict)

        # this is probably not how you're supposed to compare two arrays,
        # but right now I don't see the obvious thing, or whether it would
        # be okay to use numpy.testing and it's operations like "assertAlmostAllEqual"
        self.assertEqual(0.0, np.max(np.abs(experimental_value - reference_value)))
