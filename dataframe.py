from file_handler import read_dtype, read_csv_file, write_file
import os

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
        # nulls_per_col = {k:[] for k in self.dtypes.keys()}
        pass
        

    
    #TODO: define describe()
        
    #TODO: define fillna()   
        
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
    
    
    
    
