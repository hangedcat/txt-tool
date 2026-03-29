class FileRecord:

    def __init__(self, file_name: str, mode: str = "read"):
        self.file_name = file_name
        self.mode = mode
        self.line_count = 0

    def __repr__(self) -> str:       
        return f"FileRecord(file_name='{self.file_name}', mode='{self.mode}', line_count={self.line_count})"

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        if mode not in ('read', 'write', 'append'):
            raise ValueError("mode should either be 'read' or 'write'.")
        self._mode = mode

    @staticmethod
    def validate_extension(file_name: str):
        return file_name.endswith(".txt")

class FileReader(FileRecord):

    def __init__(self, file_name: str):
        super().__init__(file_name, mode= 'read')

    def line_reader(self) -> int | None:
        try :
            with open(self.file_name, 'r') as f:
                i = f.readlines()
                self.line_count = len(i)
        except FileNotFoundError:
            print(f"Error : {self.file_name} not found")

class FileWriter(FileRecord):

    def __init__(self, file_name: str):
        super().__init__(file_name, mode= 'w')

    def text_writer(self, message: str) -> None:
        try:
            with open(self.file_name, 'w') as f:
                f.write(message)
                print(f"'{message}' have been written into {self.file_name}")
        except PermissionError:
            print(f"Error : you have no permission for {self.file_name}")

class FileAppender(FileRecord):

    def __init__(self, file_name: str):
        super().__init__(file_name, mode= 'a')

    def text_appender(self, message: str) -> None:
        try:
            with open(self.file_name, 'a') as f:
                f.write(message)
                print(f"'{message}' have been append into {self.file_name}")
        except PermissionError:
            print(f"Error : you have no permission for {self.file_name}")