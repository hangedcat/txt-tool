def line_reader() -> int | None:
    file_name: str = input("Please input file name: ")
    try :
        with open(file_name, 'r') as f:
            i = f.readlines()
            return len(i)
    except FileNotFoundError:
        print(f"Error : {file_name} not found")

if __name__ == "__main__" :
    line_reader()