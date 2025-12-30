from re import S
import pandas as pd
from pandas.core.arrays import categorical

from services.profiling import InnoProfiler
from services.profiling.internal import inno

from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import os
from matplotlib import pyplot as plt
import multiprocessing as mp
import numpy as np

class InnoAnalyzer:

    def __init__(self,inno_data : InnoProfiler): # Dependency Injection
        self.profiler_data = inno_data
        self.workbook = load_workbook(os.path.join(self.profiler_data.out_dir,"DataAnalysis.xlsx"))
    
    def get_safe_column(self,column):
        return column.replace(" ","_").replace("*","_")
    
    def plot_numerical_column(self,column):
        self.profiler_data.data[column].plot.hist(bins=10,figsize=(6,4))
        plt.axvline(self.profiler_data.data[column].mean(),color="red")
        plt.axvline(self.profiler_data.data[column].median(),color="green")
        plt.xlabel(f"{column}-data")
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(self.profiler_data.out_dir,f"{self.get_safe_column(column)}_hist.png"))

    # Write a function to create a bar plot on a categrical variable upon applying value_counts() on it.
    def plot_categorical_column(self,column):
        self.profiler_data.data[column].value_counts().plot.bar(figsize=(6,4))
        plt.xlabel(f"{column}-data")
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(self.profiler_data.out_dir,f"{self.get_safe_column(column)}_bar.png"))

    def plot_adv_stats(self,args):
        column = args[0]
        rv = args[1]
        fig,axes = plt.subplots(2,2,figsize=(10,6))
        axes[0][0].plot(self.profiler_data.numerical_columns_stats[column]["real_time_values"],
                        self.profiler_data.numerical_columns_stats[column][f"real_time_values_{rv}_pmfs"])
        axes[0][0].axvline(self.profiler_data.numerical_columns_stats[column]["real_time_values"].mean(),color="red",linestyle="--",label="mean")
        axes[0][0].axvline(self.profiler_data.numerical_columns_stats[column]["real_time_values"].std(),color="green",linestyle="--",label="std")
        axes[0][0].axvspan(abs(self.profiler_data.numerical_columns_stats[column]["real_time_values"].mean()-self.profiler_data.numerical_columns_stats[column]["real_time_values"].std()),abs(self.profiler_data.numerical_columns_stats[column]["real_time_values"].mean()+self.profiler_data.numerical_columns_stats[column]["real_time_values"].std()),alpha=0.1,color="blue")
        axes[0][0].set_title(f"{rv.capitalize()} PMF Distribtion of {self.get_safe_column(column)} Column")
        axes[0][0].legend()
        axes[0][1].plot(self.profiler_data.numerical_columns_stats[column]["real_time_values"],self.profiler_data.numerical_columns_stats[column][f"real_time_values_{rv}_cdfs"])
        axes[0][1].axvline(self.profiler_data.numerical_columns_stats[column]["real_time_values"].mean(),color="red",linestyle="--",label="mean")
        axes[0][1].axvline(self.profiler_data.numerical_columns_stats[column]["real_time_values"].std(),color="green",linestyle="--",label="std")
        axes[0][1].set_yticks(np.linspace(0,1,11))
        axes[0][1].set_title(f"{rv.capitalize()} CDF Distribtion of {self.get_safe_column(column)} Column")
        axes[0][1].legend()


        axes[1][0].plot(self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"],self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}_pmfs"])
        axes[1][0].axvline(self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"].mean(),color="red",linestyle="--",label="mean")
        axes[1][0].axvline(self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"].std(),color="green",linestyle="--",label="std")
        axes[1][0].axvspan(abs(self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"].mean()-self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"].std()),
                        abs(self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"].mean()+self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"].std()),alpha=0.1,color="blue")
        axes[1][0].set_title(f"{rv.capitalize()} PMF Distribtion of {self.get_safe_column(column)} Column")
        axes[1][0].legend()
        axes[1][1].plot(self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"],self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}_cdfs"])
        axes[1][1].axvline(self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"].mean(),color="red",linestyle="--",label="mean")
        axes[1][1].axvline(self.profiler_data.numerical_columns_stats[column][f"theor_values_{rv}"].std(),color="green",linestyle="--",label="std")
        axes[1][1].set_title(f"{rv.capitalize()} CDF Distribtion of {self.get_safe_column(column)} Column")
        axes[1][1].legend()
        plt.tight_layout()
        plt.savefig(os.path.join(self.profiler_data.out_dir,f"{self.get_safe_column(column)}_{rv}_stats.png"))

    def analyze(self):
        numerical_sheet = self.workbook["NumericalColumnStats"]
        categorical_sheet = self.workbook["CategoricalColumnStats"]

        self.profiler_data.data[self.profiler_data.numerical_columns[0]].plot.hist(figsize=(15,8))
        
        with mp.Pool(processes=mp.cpu_count()-1) as pool:
            pool.map(self.plot_numerical_column,self.profiler_data.numerical_columns)

        with mp.Pool(processes=mp.cpu_count()-1) as pool:
            pool.map(self.plot_adv_stats,zip(self.profiler_data.numerical_columns,["poisson"]*len(self.profiler_data.numerical_columns)))

        with mp.Pool(processes=mp.cpu_count()-1) as pool:
            pool.map(self.plot_adv_stats,zip(self.profiler_data.numerical_columns,["norm"]*len(self.profiler_data.numerical_columns)))

        with mp.Pool(processes=mp.cpu_count()-1) as pool:
            pool.map(self.plot_categorical_column,self.profiler_data.categorical_columns)



        i = 2
        for column in self.profiler_data.numerical_columns:
            image = Image(os.path.join(self.profiler_data.out_dir,f"{self.get_safe_column(column)}_hist.png"))
            numerical_sheet.add_image(image,f'K{i}')
            i += 30

        i = 2
        for column in self.profiler_data.categorical_columns:
            image = Image(os.path.join(self.profiler_data.out_dir,f"{self.get_safe_column(column)}_bar.png"))
            categorical_sheet.add_image(image,f'K{i}')
            i += 30

        self.workbook.save(os.path.join(self.profiler_data.out_dir,"DataAnalysis.xlsx"))        