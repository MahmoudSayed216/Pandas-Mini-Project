import csv

def read_csv_file(file_path, dtypes:dict):
    """
    Read a CSV file and convert each column to the specified data type.

    Args:
        file_path (str): Path to the CSV data file.
        dtypes (dict): Dictionary mapping column names to data types ('int', 'float', 'string').

    Returns:
        dict: A dictionary where keys are column names and values are lists of column values.
              Missing values (empty strings) are replaced with None.
    
    """
    pass

def read_dtype(file_path):
    dtypes = {}
    
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            dtypes[row['column']] = row['dtype']


    return dtypes
    








            
def write_file(file_path, data:dict):
    """
    Write a data dictionary to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (dict): Dictionary where keys are column names and values are lists of column values.

    Returns:
        None
    """
    pass
