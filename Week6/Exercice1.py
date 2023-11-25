'''
Create a Python script that does the following:
Takes a directory path and a file extension as command line arguments (use sys.argv).
Searches for all files with the given extension in the specified directory (use os module).
For each file found, read its contents and print them.
Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.
'''

import os
import sys

def read_files(directory, extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if filename.endswith(extension):
                try:
                    with open(file_path, 'r') as file:
                        print(f"\nContents of {filename}:\n")
                        print(file.read())
                except Exception as e:
                    print(f"Error reading file '{filename}': {e}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except NotADirectoryError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        read_files(directory_path, file_extension)
