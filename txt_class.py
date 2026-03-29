class FileRecord:

    def __init__(self, file_name: str, mode: str = "read"):

        self.file_name = file_name
        self.mode = mode
        self.line_count = 0

    def __repr__(self) -> str:
        
        return f"FileRecord(file_name='{self.file_name}', mode='{self.mode}', line_count={self.line_count})"
    
    def update_count(self, count: int) -> None:

        self.line_count = count

    def line_reader(self):
        
        try :
            with open(self.file_name, 'r') as f:
                i = f.readlines()
                self.line_count = len(i)
        except FileNotFoundError:
            print(f"Error : {self.file_name} not found")

    def text_writer(self, message: str):

        if self.mode.lower() == "write":
            mode = 'w'
        elif self.mode.lower() == 'append':
            mode = 'a'
        else:
            return print(f"'{self.mode}' is not valid.")

        try:
            with open(self.file_name, mode) as f:
                f.write(message)
                print(f"'{message}' have been written into {self.file_name}")
        except PermissionError:
            print(f"Error : you have no permission for {self.file_name}")


File_1 = FileRecord(file_name="text.txt", mode="sama")
File_2 = FileRecord(file_name="text.txt", mode="read")

x = File_1.line_reader()
File_1.text_writer(message="hdjahsdja")

print(File_1)
print(File_2)