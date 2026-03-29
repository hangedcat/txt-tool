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

    def update_count(self, count: int) -> None:

        self.line_count = count

    def line_reader(self) -> int | None:
        
        try :
            with open(self.file_name, 'r') as f:
                i = f.readlines()
                self.line_count = len(i)
        except FileNotFoundError:
            print(f"Error : {self.file_name} not found")

    def text_writer(self, message: str) -> None:

        if self.mode.lower() == "write":
            mode = 'w'
        elif self.mode.lower() == 'append':
            mode = 'a'
        else:
            print(f"'{self.mode}' is not valid.")
            return

        try:
            with open(self.file_name, mode) as f:
                f.write(message)
                print(f"'{message}' have been written into {self.file_name}")
        except PermissionError:
            print(f"Error : you have no permission for {self.file_name}")

f1 = FileRecord("text.txt", "read")

print(f1.mode)
