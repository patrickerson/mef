


class FileManipulation:

    def __init__(self, filename, ext=".txt"):
        self.filename = filename + ext

    def decode_file(self):
        file_content = self.read_file()
        return file_content.split('\n')[1:]

    def read_file(self):
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            print("file don't exist")
            return "file don't exist"
    
    def get_filename(self):
        return self.filename

    def count_lines(self):
        decode_file = self.decode_file()
        num_lines = len(decode_file) - 1
        if num_lines == 0:
            return "File is empty"
        if int(decode_file[0]) != num_lines:
            return "Number of lines is wrong"
        return num_lines