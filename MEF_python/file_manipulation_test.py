import unittest
from file_manipulation import FileManipulation

class TestWFileManiputation(unittest.TestCase):

    def test_open_file(self):
        read_file_test = FileManipulation("test_files/read_file_test1")
        invalid_file = FileManipulation("test_files/invalid_file")
        self.assertEqual(read_file_test.read_file(), "test file read working")
        self.assertEqual(invalid_file.read_file(), "file don't exist")

    def test_lines_counter(self):
        count_lines_test1 =  FileManipulation("test_files/count_lines_test1")
        count_lines_test2 =  FileManipulation("test_files/count_lines_test2")
        count_lines_test3 =  FileManipulation("test_files/count_lines_test3")
        count_lines_test4 =  FileManipulation("test_files/count_lines_test4")
        self.assertEqual(count_lines_test1.count_lines(), 3)
        self.assertEqual(count_lines_test2.count_lines(), "Number of lines is wrong")
        self.assertEqual(count_lines_test3.count_lines(), "Number of lines is wrong")
        self.assertEqual(count_lines_test4.count_lines(), "File is empty")


if __name__ == '__main__':
    unittest.main()