import csv

def read_csv_file(file_path, dtypes:dict):
    data = {k:[] for k in dtypes.keys()}
    def process_row(row: dict):
        for key, val in row.items():
            if dtypes[key] == 'int':
                if row[key] == '':
                    row[key] = None
                else:
                    row[key] = int(row[key])

            elif dtypes[key] == 'float':
                if row[key] == '':
                    row[key] = None
                else:
                    row[key] = float(row[key])
            elif dtypes[key] == 'string':
                if row[key] == 'None' or row[key] == 'NULL' or row[key] == 'N/A' or row[key] == '' or row[key].strip() == '':
                    row[key] = None

    def add_row_to_container(row:dict):
        for key, value in row.items():
            data[key].append(value)
    
    with open(file_path) as csvfile:
        
        reader = csv.DictReader(csvfile)
        # i = 0
        for row in reader:
            process_row(row)
            add_row_to_container(row)

    return data

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
