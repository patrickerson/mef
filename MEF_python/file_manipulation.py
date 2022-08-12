


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
