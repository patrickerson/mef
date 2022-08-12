from MEF_python.file_manipulation import FileManipulation
import MEF_python.MEF as mef

EXERCISE_FILES = "MEF_python/exercise_test_files/"

def print_decoded_file(File):
    print(f"{File.get_filename()}\n")
    for line in File.decode_file():
        print(mef.check_language(line))
    print("\n")
    print("_"*50)
    print("\n")

def init_program():
    test1 = FileManipulation(f"{EXERCISE_FILES}test1")
    test2 = FileManipulation(f"{EXERCISE_FILES}test2")
    test3 = FileManipulation(f"{EXERCISE_FILES}test3")
    teacher_file = FileManipulation(f"{EXERCISE_FILES}teacher_file")

    print_decoded_file(test1)
    print_decoded_file(test2)
    print_decoded_file(test3)
    print_decoded_file(teacher_file)

    print("Type a filename to open a custom file with the program.")
    print("Example:")
    print("'my_file' to access my_file.txt")
    custom_name_file = input("\ncustom filename (insert 'c' to cancel): ")
    if custom_name_file != "c":
        custom_file = FileManipulation(custom_name_file)
        print_decoded_file(custom_file)
    print("End")
