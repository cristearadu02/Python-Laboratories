class CSVValidator:
    """
    CSVValidator class for reading and validating CSV files based on user-defined rules.
    """

    def __init__(self, file_path):
        """
        Initialize CSVValidator with the given file path.

        Parameters:
        - file_path (str): The path to the CSV file.
        """
        self.file_path = file_path

    def read_csv(self):
        """
        Read the CSV file and return its contents as a list of lists.

        Returns:
        - list: A list of lists representing the rows and columns of the CSV file.
        """
        data = []
        with open(self.file_path, 'r') as file:
            for line in file:
                # Split the line into values
                values = line.strip().split(',')
                data.append(values)
        return data

    def validate(self, rules):
        """
        Validate the CSV file based on user-defined rules.

        Parameters:
        - rules (dict): A dictionary containing validation rules.
                       Example:
                       {
                           'check_missing': True,  # Check for missing values
                           'column_types': {       # Define expected data types for each column
                               0: int,             # Column 0 should be an integer
                               1: str,             # Column 1 should be a string
                               # Add more columns as needed
                           }
                       }

        Returns:
        - bool: True if the CSV file passes all validation checks, False otherwise.
        """
        data = self.read_csv()
        header_length = len(data[0]) if data else 0

        for row_index, row in enumerate(data):
            # skip the header
            if row_index == 0:
                continue
            if len(row) != header_length:
                print(f"Error: Row {row_index + 1} does not have the same number of parameters as the header.")
                return False

            for col_index, value in enumerate(row):
                if rules.get('check_missing') and not value:
                    print(f"Error: Missing value at Row {row_index + 1}, Column {col_index + 1}")
                    return False

                expected_type = rules.get('column_types', {}).get(col_index)
                if expected_type:
                    try:
                        converted_value = expected_type(value)
                    except ValueError:
                        print(f"Error: Incorrect data type at Row {row_index + 1}, Column {col_index + 1}. "
                              f"Expected type: {expected_type.__name__}, Actual type: {type(value).__name__}")
                        return False

        # If no errors were found, return True
        return True
