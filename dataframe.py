from file_handler import read_dtype, read_csv_file, write_file
import os
from functools import reduce
import stats

class Dataframe:
    def __init__(self, data:dict, dtypes:dict):
        self.data = data
        self.dtypes = dtypes
    
    #TODO: define read_csv(data_path, dtype_path)
    @classmethod
    def read_csv(cls, data_path: str, dtype_path: str):
        
        dtypes = read_dtype(dtype_path)
        data = read_csv_file(data_path, dtypes)

        return Dataframe(data = data, dtypes = dtypes)

    #TODO: define count_nulls()
    def count_null(self):
        nulls_per_col = {k:[] for k in self.dtypes.keys()}
        for key in self.dtypes.keys():
            column = self.data[key]
            nulls_sum = reduce(lambda x, y : x + (1 if y is None else 0), column, 0)
            nulls_per_col[key] = nulls_sum

        return nulls_per_col

    
    #TODO: define describe()
        
    def describe(self, path: str):

        for key, val in self.dtypes.items():
            if self.dtypes[key] == 'float' or self.dtypes[key] == 'int':
                pass
            else:
                pass
    
    #TODO: define fillna()
    def fillna(self, num_strat, cat_strat):
        if num_strat is not None:
            if num_strat not in [stats.get_col_max, stats.get_col_mean, stats.get_col_median, stats.get_col_min, stats.get_col_mode, stats.get_stat]:
                raise ValueError("function must be within this list of function [stats.get_col_max, stats.get_col_mean, stats.get_col_median, stats.get_col_min, stats.get_col_mode, stats.get_stat]")
        if cat_strat is not None:
            if cat_strat != stats.get_col_mode:
                raise ValueError("Can't compute this stat for a column of type string")
            




        


    #TODO: define to_csv()
    # def head(length):


    def __str__(self):
        s = "\t|".join([key for key in self.data.keys()])
        rows = [s]

        for i in range(len(self.data[list(self.data.keys())[0]])):
            r = ""
            for key in self.data.keys():
                r+=str(self.data[key][0]) + "\t|"
            rows.append(r[0:-1])
        return "\n".join(rows)
    
    
    
    
