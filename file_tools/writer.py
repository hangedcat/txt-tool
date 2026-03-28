def text_writer() -> None:
    file_name: str = input("Please insert the name of the file write: ")
    message: str = input("Please insert text to write: ")

    while True:
        mode: str = input("Choose mode (Overwrite or Append): ")

        if mode.lower() == "overwrite":
            mode = 'w'
            break
        elif mode.lower() == 'append':
            mode = 'a'
            break
        else:
            print(f"'{mode}' is not valid. Please enter 'overwrite' or 'append'.")
            continue
            
    try:
        with open(file_name, mode) as f:
            f.write(message)
            print(f"'{message}' have been written into {file_name}")
    except PermissionError:
        print(f"Error : you have no permission for {file_name}")

if __name__ == "__main__" :
    text_writer()