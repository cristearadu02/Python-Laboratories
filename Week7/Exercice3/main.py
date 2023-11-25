from file_merger import merge_files, validate_file_paths

# Example file paths and output path
input_files = ['C:\\Users\\crist\\PycharmProjects\\csvValidator\\file1.txt',
               'C:\\Users\\crist\\PycharmProjects\\csvValidator\\file2.txt',
               'C:\\Users\\crist\\PycharmProjects\\csvValidator\\file3.txt']

output_file = 'C:\\Users\\crist\\PycharmProjects\\csvValidator\\merged_output.txt'

# Validate file paths
validate_file_paths(input_files)

# Merge files with a custom separator
merge_files(input_files, output_file, separator='\n---\n')

print(f"Files merged successfully. Output saved to '{output_file}'.")
