from pathlib import Path
from functools import wraps
from collections import Counter, defaultdict, deque
from typing import Union, Optional, TypeVar, Generator
import logging
import os
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FileRecord:

    def __init__(self, file_name: Union[str, Path], mode: str = "read"):
        self.file_name = file_name
        self.mode = mode
        self.line_count = 0

    def __repr__(self) -> str:       
        return f"FileRecord(file_name='{self.file_name}', mode='{self.mode}', line_count={self.line_count})"

    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, mode: str) -> None:
        if mode not in ('r', 'w', 'a'):
            raise ValueError("mode should either be 'r', 'w' or 'a'.")
        self._mode = mode

    @staticmethod
    def validate_extension(file_name: str) -> bool:
        return file_name.endswith(".txt")

class FileReader(FileRecord):

    def __init__(self, file_name: Union[str, Path]):
        super().__init__(file_name, mode= 'r')

    def line_reader(self) -> None:
        count = 0
        for line in file_line_reader(self.file_name):
            count += 1
        self.line_count = count
    
    def __enter__(self):
        try:
            self.file = open(self.file_name, "r")
            return self.file
        except FileNotFoundError:
            logger.warning(f"File not found: {self.file_name}")
            self.file = None
            return None
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

class FileWriter(FileRecord):

    def __init__(self, file_name: str):
        super().__init__(file_name, mode= 'w')

    def text_writer(self, message: str) -> None:
        try:
            with open(self.file_name, 'w') as f:
                f.write(message)
                logger.info(f"{self.file_name} written successfully")
        except PermissionError:
            logger.error(f"Permission Denied: {self.file_name}")

class FileAppender(FileRecord):

    def __init__(self, file_name: str):
        super().__init__(file_name, mode= 'a')

    def text_appender(self, message: str) -> None:
        try:
            with open(self.file_name, 'a') as f:
                f.write(message)
                logger.info(f"{self.file_name} written successfully")
        except PermissionError:
            logger.error(f"Permission Denied: {self.file_name}")


def file_line_reader(file_name: Union[str, Path]) -> Generator[str, None, None]:
    try:
        with open(file_name, 'r') as f:
            for line in f:
                yield line
    except FileNotFoundError:
        logger.warning(f"File not found: {file_name}")

def get_txt_file(folder: Path | str) -> list[Path]:
    p = Path(folder)
    return list(p.glob("*.txt"))

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug(f"{func.__name__} takes {end - start} seconds to run.")
        return result
    return wrapper

@timer
def process_folder(folder: Path | str) -> list[FileReader]:
    n = get_txt_file(folder)
    m = [FileReader(x) for x in n]
    for i in m:
        i.line_reader()
    return m

def print_report(summary: list[FileReader]) -> None:
    text = "File Batch Report"
    print(f"{text :=^50}")
    print(f"File Processed: {len(summary)}")
    print("-" * 50)
    for file in summary:
        print(f"{Path(file.file_name).name :<30} {file.line_count}")
    print("-" * 50)
    print(f"Total Lines: {sum(x.line_count for x in summary)}")

def analyze_folder(folder: Path | str) -> None:
    files = process_folder(folder)
    line_count = [file.line_count for file in files]
    analyze = Counter(line_count)
    for linecount, numfiles in analyze.most_common():
        print(f'{linecount} Line : {numfiles} File')

def tail(file_name: str, n: int) -> list[str]:
    lines = deque(maxlen=n)
    for line in file_line_reader(file_name=file_name):
        lines.append(line.strip())
    return list(lines)
