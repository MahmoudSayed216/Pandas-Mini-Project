from functools import reduce


def h_preprocess(col):
    first_non_null = None
    i = 0
    for val in col:
        if val is not None and first_non_null is None:
            first_non_null = i
        elif val is None:
            continue
        elif isinstance(val, str):
            raise TypeError("Can't Compute max for a column of string datatype")
        i+=1

    return first_non_null

def get_col_max(col:list):
    first_non_null = h_preprocess(col)
    mx = col[first_non_null]
    for i in range(first_non_null+1, len(col)):
        if  col[i] is not None and col[i] > mx:
            mx = col[i]

    return mx


def get_col_min(col:list):
    first_non_null = h_preprocess(col)
    mx = col[first_non_null]
    for i in range(first_non_null+1, len(col)):
        if  col[i] is not None and col[i] < mx:
            mx = col[i]

    return mx

def get_col_mean(col:list):
    h_preprocess(col)
    """
    Compute the mean (average) value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The mean value of the column (float).
    """
    sum_criterion = lambda x, y: x+ (y if y is not None else 0)
    count_criterion = lambda x, y: x+ (1 if y is not None else 0)
    
    sm = reduce(sum_criterion, col, 0)
    cnt = reduce(count_criterion, col, 0)

    return sm/cnt

def get_col_median(col:list):
    h_preprocess(col)
    """
    Compute the median value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The median value of the column (numeric type).
    """
    non_nulls = [v for v in col if v is not None]
    sorted_non_nulls = sorted(non_nulls)
    length = len(sorted_non_nulls)
    center = length/2
    if length%2 == 0:
        return (sorted_non_nulls[center] + sorted_non_nulls[center-1])/2
    
    return sorted_non_nulls[center]


    
def get_col_mode(col:list):
    first_non_null = h_preprocess(col)
    """
    Compute the mode (most frequent value) of a column.

    Args:
        col (list): A list of values. `None` values are ignored.

    Returns:
        The mode value of the column. If multiple values have the same
        frequency, the first encountered is returned.
    """
    freq_map = {}

    for val in col:
        if val is not None:
            if val in freq_map:
                freq_map[val]+=1
            else:
                freq_map[val] = 0

    mx = -1
    k = None
    for key, val in freq_map.items():
        if freq_map[key] > mx:
            mx = freq_map[key]
            k = key

    return freq_map[key]

    

        
def get_stat(data:dict, dtypes:dict, function):
    """
    Apply a statistical function to all numerical columns in a dataset.

    Args:
        data (dict): Dictionary where keys are column names and values are lists of column values.
        dtypes (dict): Dictionary where keys are column names and values are data types ('int', 'float', 'string').
        function (function): A function to apply to each numerical column (e.g., get_col_max, get_col_mean).

    Returns:
        dict: A dictionary where keys are column names and values are the result
        of applying the function to that column. Only numerical columns are processed.
    """
    pass





