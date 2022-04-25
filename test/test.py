import unittest
import sys
import os

sys.path.append("..")
import SeismoTools.SeismoTools as st

## Helper functions
def load_text(filename):
    with open(filename) as f:
        raw_text = f.read()
    return raw_text
def load_binary(filename):
    with open(filename, mode='rb') as f:
        filecontent = f.read()
    return filecontent
def remove_file(new_filename):
    if os.path.isfile(new_filename):
        os.remove(new_filename)

## Testing SAC
filename_sac1 = './test/SAC/sac_example_BHE.SAC'
filename_sac2 = './test/SAC/sac_example_BHN.SAC'
filename_sac3 = './test/SAC/sac_example_BHZ.SAC'
filename_sac3_json_reference = './test/json/sac_example_BHZ.json'

class TestSACFunctionExist(unittest.TestCase):
    def test_SAC2JSON(self):
        with self.assertRaises(TypeError):
            st.SAC2JSON()
class TestLoadSAC(unittest.TestCase):
    def setUp(self):
        self.raw_data = load_binary(filename_sac3)
        self.json_reference = load_text(filename_sac3_json_reference)
    def test_raw_length(self):
        self.assertEqual(len(self.raw_data), 71832)
    def test_json_length(self):
        self.assertEqual(len(self.json_reference), 272570)

## Testing NDK
filename_ndk = './test/NDK/ndk_example.txt'
filename_ndk_split = os.path.splitext(filename_ndk)
filename_ndk_json_reference = './test/json/ndk_reference.json'
filename_ndk_json_output = filename_ndk_split[0] + '.json'

class TestNDKFunctionExist(unittest.TestCase):
    def test_NDK2JSON(self):
        with self.assertRaises(TypeError):
            st.NDK2JSON()
class TestLoadNDK(unittest.TestCase):
    def setUp(self):
        self.raw_text = load_text(filename_ndk)
        self.json_reference = load_text(filename_ndk_json_reference)
    def test_raw_length(self):
        self.assertEqual(len(self.raw_text), 405)
    def test_json_length(self):
        self.assertEqual(len(self.json_reference), 1708)
class TestNDK2JSON(unittest.TestCase):
    def setUp(self):
        remove_file(filename_ndk_json_output)
        self.filename = filename_ndk
        st.NDK2JSON(filename_ndk, 0, filename_ndk_json_output)
        self.json_output = load_text(filename_ndk_json_output)
        self.json_reference = load_text(filename_ndk_json_reference)
    def tearDown(self):
        remove_file(filename_ndk_json_output)
    def test_any_change(self):
        self.assertNotEqual(load_text(self.filename), self.json_output)
    def test_correct_change(self):
        self.assertEqual(self.json_output, self.json_reference)


if __name__ == "__main__":
    unittest.main()