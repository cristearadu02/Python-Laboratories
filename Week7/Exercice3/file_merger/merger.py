def merge_files(file_paths, output_path, separator='\n'):
    """Merge multiple text files into one.

    Parameters:
    - file_paths (list): List of file paths in the desired order.
    - output_path (str): Path to the output merged file.
    - separator (str, optional): Custom separator between file contents. Defaults to a newline character.
    """
    with open(output_path, 'w') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r') as input_file:
                output_file.write(input_file.read())
                output_file.write(separator)
