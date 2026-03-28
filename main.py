from Utilities.txt_tool.file_tools.reader import line_reader
from Utilities.txt_tool.file_tools.writer import text_writer

def main():
    while True:
        print("Welcome to TXT tool!")
        print("=" * 20)
        print(f"\n1. Line Reader\n2. Text Writer\n3. Exit\n")
        print("=" * 20)
        user = input("Please choose an option: ")

        if user == "1":
            result = line_reader()
            if result is not None:
                print(result)
        elif user == "2":
            text_writer()
        elif user == "3":
            break

if __name__ == "__main__" :
    main()