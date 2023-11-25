'''
Write a Python script that counts the number of files with each extension in a given directory. The script should:
Accept a directory path as a command line argument (using sys.argv).
Use the os module to list all files in the directory.
Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.
'''

import os
import sys

def count_files(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        file_extensions = {}
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_name, file_extension = os.path.splitext(file_path)
                if file_extension not in file_extensions:
                    file_extensions[file_extension] = 1
                else:
                    file_extensions[file_extension] += 1

        for file_extension, count in file_extensions.items():
            print(f"Number of files with extension '{file_extension}': {count}")

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
        count_files(directory_path)