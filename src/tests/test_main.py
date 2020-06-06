<<<<<<< HEAD:src/test_main.py
import unittest

class TestOthers(unittest.TestCase):

    def test_DataStructures(self):
        import DataStructuresNew
        DataStructuresNew.test_DataStructures()

    def test_spike(self):
        import Test_SpikePlot

    def test_loadplot(self):
        import TestLoadPlot

    def test_curvature(self):
        import Test_Curvature

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
   unittest.main()
=======
import unittest
import sys
sys.path.append('../')

class TestOthers(unittest.TestCase):

    def test_DataStructures(self):
        from modules import DataStructures
        DataStructures.test_DataStructures()

 #   def test_spike(self):
   #     pass

    def test_loadplot(self):
        pass

    def test_curvature(self):
        pass

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
>>>>>>> upstream/master:src/tests/test_main.py
