from csv_validator.csv_validator import CSVValidator

if __name__ == "__main__":

    file_path = 'C:\\Users\\crist\\PycharmProjects\\csvValidator\\cars.csv'

    validation_rules = {
        'check_missing': True,
        'column_types': {
            0: str,
            1: int,
            2: str
        }
    }

    validator = CSVValidator(file_path)
    is_valid = validator.validate(validation_rules)

    if is_valid:
        print("CSV file is valid.")
    else:
        print("CSV file is not valid.")