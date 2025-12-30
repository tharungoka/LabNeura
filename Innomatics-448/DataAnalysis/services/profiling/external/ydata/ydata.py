from re import S
import ydata_profiling as yp
import pandas as pd

class YdataProfiler:
    def __init__(self,file_path : str, out_dir = "/Users/gtk/GTK/Innomatics-448/DataAnalysis/assets/output"):
        self.data = pd.read_csv(file_path)
        self.out_dir = out_dir
    def analyze(self):
        profile = yp.ProfileReport(self.data)
        self.report = profile.get_description()
        categories = set(map(lambda x:x[1]["type"],self.report.variables.items()))
        self.columns = {}
        for category in categories:
            self.columns[category] = list(map(lambda x:x[0],list(filter(lambda x: True if x[1]["type"]==category else False,self.report.variables.items()))))
        self.basic_details = self.report.table
        print("No of rows",self.basic_details["n"])
        print("No of columns",self.basic_details["n_var"])
        self.numerical_columns = self.columns["Numeric"]
        self.categorical_columns = self.columns["Categorical"]
        self.datetime_columns = self.columns["DateTime"]