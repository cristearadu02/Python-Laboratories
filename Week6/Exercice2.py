'''
Write a script using the os module that renames all files in a specified directory to have a sequential number prefix.
For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or files that can't be renamed.
'''

import os
import sys

def rename_files(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        count = 1
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_name, file_extension = os.path.splitext(file_path)
                os.rename(file_path, file_name + str(count) + file_extension)
                print(f"File '{filename}' renamed to '{file_name}{str(count)}{file_extension}'")
                count += 1

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
        rename_files(directory_path)