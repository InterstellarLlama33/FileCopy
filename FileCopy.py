source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

try:
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        dest.write(src.read())
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
