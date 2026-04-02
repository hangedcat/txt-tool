from pathlib import Path
from functools import wraps
import os
import time


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
        if mode not in ('r', 'w', 'a'):
            raise ValueError("mode should either be 'r', 'w' or 'a'.")
        self._mode = mode

    @staticmethod
    def validate_extension(file_name: str):
        return file_name.endswith(".txt")

class FileReader(FileRecord):

    def __init__(self, file_name: str):
        super().__init__(file_name, mode= 'r')

    def line_reader(self) -> int | None:
        count = 0
        for line in file_line_reader(self.file_name):
            count += 1
        self.line_count = count

def file_line_reader(file_name: str):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                yield line
    except FileNotFoundError:
        print(f'"{file_name}" not found!')

def get_txt_file(folder: str) -> list:
    p = Path(folder)
    return list(p.glob("*.txt"))

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} takes {end - start} seconds to run.")
        return result
    return wrapper

@timer
def process_folder(folder: str):
    n = get_txt_file(folder)
    m = [FileReader(x) for x in n]
    for i in m:
        i.line_reader()
    return m

def print_report(summary: list):
    text = "File Batch Report"
    print(f"{text :=^50}")
    print(f"File Processed: {len(summary)}")
    print("-" * 50)
    for file in summary:
        print(f"{Path(file.file_name).name :<30} {file.line_count}")
    print("-" * 50)
    print(f"Total Lines: {sum(x.line_count for x in summary)}")

i = process_folder('D:/Project')
print_report(i)

