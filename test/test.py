import unittest
import sys

sys.path.append("..")
import SeismoTools.SeismoTools as st

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.var = 1
    def test_var(self):
        self.assertEqual(self.var, 1)

class TestFunctionExist(unittest.TestCase):
    def test_SAC2JSON(self):
        with self.assertRaises(TypeError):
            st.SAC2JSON()
    def test_NDK2JSON(self):
        with self.assertRaises(TypeError):
            st.NDK2JSON()


if __name__ == "__main__":
    unittest.main()
