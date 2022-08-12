import unittest
from file_manipulation import FileManipulation

class TestWFileManiputation(unittest.TestCase):

    def test_open_file(self):
        read_file_test = FileManipulation("MEF_python/test_files/read_file_test1", ext="")
        invalid_file = FileManipulation("test_files/invalid_file")
        self.assertEqual(read_file_test.read_file(), "test file read working")
        self.assertEqual(invalid_file.read_file(), "file don't exist")


if __name__ == '__main__':
    unittest.main()