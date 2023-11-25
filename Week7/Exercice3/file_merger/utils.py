import os


def validate_file_paths(file_paths):
    """Validate that all file paths exist."""
    for file_path in file_paths:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
