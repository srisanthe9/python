import os

directory_path = '/path/to/your/directory'

try:
    contents = os.listdir(directory_path)
    print(f"Contents of the directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access the directory '{directory_path}'.")
