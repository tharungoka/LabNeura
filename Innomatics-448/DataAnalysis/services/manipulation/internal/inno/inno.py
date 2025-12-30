from services.profiling import InnoProfiler
from scipy.stats.mstats import gmean
from services.profiling.internal import inno

import numpy as np
import pandas as pd
from scipy.stats import boxcox

class InnoManipulator:
    
    def __init__(self,inno_profiler : InnoProfiler):
        self.inno_profiler = inno_profiler
    
    def manipute_numerical_column(self,column):
        print(f"[INFO] Missing values of the numerical column {column} can be filled using following")
        print("1. Mean\n2.Median\3.Geomean")
        status = True
        # Remove While loop
        while status:
            try:
                choice = int(input("Please choose 1/2/3 (Press enter to default (mean))"))
                if choice == 1:
                    self.inno_profiler.data[column].fillna(self.inno_profiler.data[column].mean(),inplace=True)
                elif choice == 2:
                    self.inno_profiler.data[column].fillna(self.inno_profiler.data[column].median(),inplace=True)
                elif choice == 3:
                    self.inno_profiler.data[column].fillna(gmean(self.inno_profiler.data[column].apply(lambda x:np.nan if x<=0 else x).dropna()))
                else:
                    self.inno_profiler.data[column].fillna(self.inno_profiler.data[column].mean(),inplace=True)

                status = False
                # log Transfromation
                negative_values = (self.inno_profiler.data[column]<0).sum()
                if not negative_values:
                    self.inno_profiler.data[f"{column}_log_transform"] = np.log(self.inno_profiler.data[column]+1e-5)
                    self.inno_profiler.data[f"{column}_boxcox_transform"] = boxcox(self.inno_profiler.data[column],0.5)
                self.inno_profiler.data[f"{column}_std_transform"] = (self.inno_profiler.data[column]-self.inno_profiler.data[column].mean())/self.inno_profiler.data[column].std()
                self.inno_profiler.data[f"{column}_minmax_transform"] = (self.inno_profiler.data[column]-self.inno_profiler.data[column].min)/(self.inno_profiler.data[column].max()-self.inno_profiler.data[column].min())
            except Exception as e:
                print("Invalid choice!!")

    def manipulate_categorical_column(self,column):
        print(f"[INFO] Missing values of the categorical column {column} can be filled using following")
        print("1. Mode (Default: Mode)")
        status = True
        while status:
            try:
                choice = int(input("Please choose 1 (Press enter to default (mode))"))
                if choice == 1:
                    self.inno_profiler.data[column].fillna(self.inno_profiler.data[column].mode(),inplace=True)
                else:
                    self.inno_profiler.data[column].fillna(self.inno_profiler.data[column].mode(),inplace=True)

                status = False

            except Exception as e:
                print("Invalid choice!!")

    def manipulate(self):
        for column in self.inno_profiler.numerical_columns + self.inno_profiler.categorical_columns:
            missing_values = self.inno_profiler.data[column].isna().sum()
            if missing_values:
                print(f"[WARN] Found a missing column {column} and no missing values are {missing_values}")
                if column in self.inno_profiler.numerical_columns:
                    self.manipute_numerical_column(column)

                if column in self.inno_profiler.categorical_columns:
                    self.manipulate_categorical_column(column)
        self.manipulate_date_time()
        # Write logic for finding duplicate rows and ask user either to discard or keep
        ## Dump the self.inno_profiler.data data frame object to excel sheet with sheet name as manipualkated dataset.
        self.inno_profiler.data
    
    def manipulate_date_time(self):
        if self.inno_profiler.datetime_columns:
            print(f"[INFO] -  Found datetime columns : {self.inno_profiler.datetime_columns}")
            choice = input(f"Do you want me to typecast to datetime..?(Y/N)")
            if choice.lower() == "y":
                for column in self.inno_profiler.datetime_columns:
                    try:
                        self.inno_profiler.data[column] = pd.to_datetime(self.inno_profiler.data[column])
                        print(f"[INFO] - column {column} is converted to datetime")
                    except Exception as e:
                        print(f"[WARN] - Issue found while converting column {column} to datetime")
