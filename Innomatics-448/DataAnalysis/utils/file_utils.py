## Write functions for following: 
### Check whether the provided filepaths exists or not
### Check what types of the file (csv, xlsx, tsv,)
#### Write corresponding reading in pandas.
    ## pd.read_csv()
    ## pd.read_excel()

import os
import pandas as pd

class FileUtils:

    @staticmethod
    def is_file_exist(filepath : str):
        status = os.path.isfile(filepath)
        return status
    
    @staticmethod
    def check_file_type(filepath : str):
        splits = filepath.split(".")
        if len(splits) > 1:
            if splits[-1] == "csv":
                return "csv"
            elif splits[-1] == "xlsx":
                return "xlsx"
            elif splits[-1] == "xls":
                return "xls"
            else:
                return ""
        else:
            return ""

    @staticmethod 
    def read_data(filepath : str):
        file_type = FileUtils.check_file_type(filepath)
        df = pd.DataFrame()
        if file_type == "csv":
            df = pd.read_csv(filepath)
        elif file_type == "xlsx":
            df = pd.read_excel(filepath,engine="openpyxl")
        elif file_type == "xls":
            df = pd.read_excel(file_type,engine="xlrd")
        elif file_type == "":
            df = pd.DataFrame()
        return df    
