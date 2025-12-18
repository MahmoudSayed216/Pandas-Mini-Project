from file_handler import read_dtype, read_csv_file, write_file
from functools import reduce
import stats
import csv

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
    def count_nulls(self):
        nulls_per_col = {k:[] for k in self.dtypes.keys()}
        for key in self.dtypes.keys():
            column = self.data[key]
            nulls_sum = reduce(lambda x, y : x + (1 if y is None else 0), column, 0)
            nulls_per_col[key] = nulls_sum

        return nulls_per_col

    
    #TODO: define describe()
        
    def describe(self, path: str):
        path+='/description.csv'
        print(path)
        nulls = self.count_nulls()
        # stats_per_col = {k:[nulls[k]] for k in self.dtypes.keys()}
        stats_per_col = []
        stat_funcs = [(stats.get_col_max, 'max'), (stats.get_col_min, 'min'), (stats.get_col_mean, 'mean'), (stats.get_col_median, 'median'), (stats.get_col_mode, 'mode')]
        
        for key, val in self.dtypes.items():
            col_stats = {}
            col_stats['column'] = key
            print(f"key: {key} \t val: {val}")
            # print(val)
            for stat_func in stat_funcs: 
                if val == 'float' or val == 'int':
                    v = stat_func[0](self.data[key])
                    col_stats[stat_func[1]] = str(v)
                else:
                    col_stats[stat_func[1]] = ''

            stats_per_col.append(col_stats)
        
        for i in range(len(stats_per_col)):
            col_name = stats_per_col[i]['column']
            stats_per_col[i]['nulls'] = nulls[col_name]
            

        with open(path, 'w', newline='') as csvfile:
            fieldnames = ['column', 'nulls', 'max', 'min', 'mean', 'median', 'mode']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(stats_per_col)




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
    
    
    
    
