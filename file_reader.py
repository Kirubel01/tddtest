import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_reader.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    read_file(filename)
