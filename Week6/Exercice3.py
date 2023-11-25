'''
Create a Python script that calculates the total size of all files in a directory provided as a command line argument.
The script should:
Use the sys module to read the directory path from the command line.
Utilize the os module to iterate through all the files in the given directory and its subdirectories.
Sum up the sizes of all files and display the total size in bytes.
Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.
'''

import os
import sys

def get_total_size(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        total_size = 0
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)

        print(f"Total size of all files in '{directory}': {total_size} bytes")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except NotADirectoryError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        get_total_size(directory_path)
