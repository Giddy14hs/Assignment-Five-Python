def create_and_write_file():
    try:
        # Creating a new file and writing to it
        with open("my_file.txt", 'w') as file:
            file.write("Line 1: This is a sample text.\n")
            file.write("Line 2: The number is 42.\n")
            file.write("Line 3: Python is fun!\n")
        print("File created and initial content written.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist. Please create the file first.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Line 4: Appending more content.\n")
            file.write("Line 5: Appending another line.\n")
            file.write("Line 6: The final line.\n")
        print("Additional content appended to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

if __name__ == "__main__":
    create_and_write_file()
    
    read_file()
    
    append_to_file()
    
    read_file()
