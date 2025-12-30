from re import S

from pandas.io import orc
from utils import FileUtils
import pandas as pd
import numpy as np
from scipy.stats.mstats import gmean
from scipy.stats import (
    poisson,
    skew,
    kurtosis,
    norm,
    binom,
    multinomial
)
import math

import os

class InnoProfiler:

    def __init__(self,file_path : str, out_dir = "/Users/gtk/GTK/Innomatics-448/DataAnalysis/assets/output"):
        self.filepath = file_path
        self.out_dir = out_dir
        self.std_mean_variance_threshold = 50 

    def get_data(self):
        status = FileUtils.is_file_exist(self.filepath)
        if status:
            self.data = FileUtils.read_data(self.filepath)
        else:
            self.data = pd.DataFrame()
        return self.data
    
    def is_numerical(self, column_name):
        try:
            temp = self.data[column_name].apply(lambda x:np.nan if (x is None or (x == np.nan)) else float(x))
            del temp
            return True
        except Exception as e:
            return False
        
    # def is_categorical(self, x):
    #     return not self.is_numerical(x) 
    
    def get_basic_details(self):
        print(f"No of Rows : {self.data.shape[0]}")
        print(f"No of Columns : {self.data.shape[1]}")
        self.numerical_columns = list(filter(self.is_numerical,self.data.columns))
        self.categorical_columns = list(filter(lambda x:not self.is_numerical(x), self.data.columns))
        print("Numerical Columns : ", self.numerical_columns)
        print("Categorical Columns : ", self.categorical_columns)
        if (len(self.numerical_columns)) == self.data.shape[1]:
            print("[WARNING] - Data conatains only numerical")
        if (len(self.categorical_columns)) == self.data.shape[1]:
            print("[WARNING] - Data contains only categorical")
        
        print("Sample Data:")
        print(self.data.head(5).to_markdown())

        self.duplicate_rows = self.data[self.data.duplicated()]
        print("Duplicated Rows:")
        print(self.duplicate_rows.to_markdown())
        self.basic_stats = {}
        self.basic_stats["No of Rows"] = self.data.shape[0]
        self.basic_stats["No of Columns"] = self.data.shape[1]
        self.basic_stats["No of Numerical Columns"] = len(self.numerical_columns)
        self.basic_stats["No of Categorical Columns"] = len(self.categorical_columns)
        self.no_missig_rows = (self.data.isna().sum(axis=1)!=0).sum()
        self.basic_stats["No of Missing Rows"] = self.no_missig_rows
        self.no_missing_cols = (self.data.T.isna().sum(axis=1)!=0).sum()
        self.basic_stats["No of Missing Columns"] = self.no_missing_cols
        self.no_duplicate_rows = self.data.duplicated().sum()
        self.basic_stats["No of Duplicate Rows"] = self.no_duplicate_rows
        self.no_duplicate_cols = self.data.T.duplicated().sum()
        self.basic_stats["No of Duplicate Cols"] = self.no_duplicate_cols
        
        self.basic_stats_df = pd.DataFrame(self.basic_stats,index=["#"]).T

    def factorial(self,x):
        n = 1
        for i in range(2,x+1):
            n *= i
        return n
    def find_poisson_pmf(self,x,lambda_):
        return math.exp(x)*(lambda_ ** x)/self.factorial(x)
    
    def get_adv_analysis(self,column,rv):
        real_time_values = self.data[column].drop(self.numerical_columns_stats[column]["outliers_indices"],axis=0).fillna(self.data[column].mean()).unique()
        real_time_values.sort()
        actual_mean = real_time_values.mean()
        actual_std = real_time_values.std()
        self.numerical_columns_stats[column]["real_time_values"] = real_time_values
        if rv == "poisson":
            self.get_poission_dist_analysis(column,actual_mean,real_time_values)
        elif rv == "norm":
            self.get_normal_dist_analysis(column,actual_mean,actual_std,real_time_values)

    def get_normal_dist_analysis(self,column,mu,std,real_time_values):
        theor_values = norm.rvs(loc=mu,scale=std,size=len(real_time_values))
        theor_values.sort()
        self.numerical_columns_stats[column]["theor_values_norm"] = theor_values
        self.numerical_columns_stats[column]["real_time_values_norm_pmfs"] = norm.pdf(real_time_values,loc=mu,scale=std)
        self.numerical_columns_stats[column]["real_time_values_norm_cdfs"] = norm.cdf(real_time_values,loc=mu,scale=std)
        self.numerical_columns_stats[column]["theor_values_norm_pmfs"] = norm.pdf(theor_values,loc=mu,scale=std)
        self.numerical_columns_stats[column]["theor_values_norm_cdfs"] = norm.cdf(theor_values,loc=mu,scale=std)
        
        self.numerical_columns_stats[column]["real_time_values_norm_skew"] = skew(real_time_values)
        self.numerical_columns_stats[column]["real_time_values_norm_kurtosis"] = kurtosis(real_time_values)

        self.numerical_columns_stats[column]["theor_values_norm_mean"] = theor_values.mean()
        self.numerical_columns_stats[column]["theor_values_norm_std"] = theor_values.std()
        self.numerical_columns_stats[column]["theor_values_norm_skew"] = skew(theor_values)
        self.numerical_columns_stats[column]["theor_values_norm_kurtosis"] = kurtosis(theor_values)

    def get_poission_dist_analysis(self,column,lambda_,real_time_values):
        theor_values = poisson.rvs(lambda_,size=len(real_time_values))
        theor_values.sort()
        # real_time_values_pmfs = []
        # real_time_values_cdfs = []
        # can be optimized using map and lambda
        # map(lambda x:find_poission_pmf,real_time_values)
        # for value in real_time_values:
        #     real_time_values_pmfs.append(poisson.pmf(value,lambda_))
        #     real_time_values_cdfs.append(poisson.cdf(value,lambda_))
        # We can use numpy vectorization
        self.numerical_columns_stats[column]["theor_values_poisson"] = theor_values
        self.numerical_columns_stats[column]["poission_lambda"] = lambda_
        self.numerical_columns_stats[column]["real_time_values_poisson_pmfs"] = poisson.pmf(real_time_values,lambda_)
        self.numerical_columns_stats[column]["real_time_values_poisson_cdfs"] = poisson.cdf(real_time_values,lambda_)
        # theor_values_pmfs = []
        # theor_values_cdfs = []
        # for value in theor_values:
        #     theor_values_pmfs.append(poisson.pmf(value,lambda_))
        #     theor_values_cdfs.append(poisson.cdf(value,lambda_))
        self.numerical_columns_stats[column]["theor_values_poisson_pmfs"] = poisson.pmf(theor_values,lambda_)
        self.numerical_columns_stats[column]["theor_values_poisson_cdfs"] = poisson.cdf(theor_values,lambda_)
        
        self.numerical_columns_stats[column]["real_time_values_poisson_skew"] = skew(real_time_values)
        self.numerical_columns_stats[column]["real_time_values_poissoin_kurtosis"] = kurtosis(real_time_values)

        self.numerical_columns_stats[column]["theor_values_poisson_mean"] = theor_values.mean()
        self.numerical_columns_stats[column]["theor_values_poisson_std"] = theor_values.std()
        self.numerical_columns_stats[column]["theor_values_poisson_skew"] = skew(theor_values)
        self.numerical_columns_stats[column]["theor_values_poisson_kurtosis"] = kurtosis(theor_values)


    def get_numerical_analysis(self):
        self.numerical_columns_stats = {}
        for column in self.numerical_columns:
            self.numerical_columns_stats[column] = {}
            self.numerical_columns_stats[column]["Mean"] = round(self.data[column].mean(),2)
            self.numerical_columns_stats[column]["Median"] = round(self.data[column].median(),2)
            self.numerical_columns_stats[column]["GeoMean"] = round(gmean(self.data[column].apply(lambda x:np.nan if x<=0 else x).dropna()),2)
            self.numerical_columns_stats[column]["std"] = round(self.data[column].std(),2)
            self.numerical_columns_stats[column]["variance"] = round(self.data[column].var(),2)
            self.numerical_columns_stats[column]["min"] = round(self.data[column].min())
            self.numerical_columns_stats[column]["max"] = round(self.data[column].max())
            self.numerical_columns_stats[column]["range"] = self.numerical_columns_stats[column]["max"] - self.numerical_columns_stats[column]["min"]
            self.numerical_columns_stats[column]["quartile-25"] = self.data[column].quantile(0.25)
            self.numerical_columns_stats[column]["quartile-50"] = self.data[column].quantile(0.5)
            self.numerical_columns_stats[column]["quartile-75"] = self.data[column].quantile(0.75)
            self.get_numerical_outliers(column)
            self.get_adv_analysis(column,"poisson")
            self.get_adv_analysis(column,"norm")

        print("Basic Stats for Numerical Columns :")
        self.numerical_stats_df = pd.DataFrame(self.numerical_columns_stats)
        print(list(map(lambda x:type(x),self.numerical_stats_df.columns)))
        print(self.numerical_stats_df.applymap(lambda x:f"{x}" if type(x)==np.ndarray else x).to_markdown())

    def get_adv_stats_categorical(self,column):
        unique_values = self.data[column].unique().shape[0]
        if unique_values == 2:
            self.get_binomial_analysis(column)
        elif unique_values > 2:
            self.get_multinomial_analysis(column)
        
    def get_multinomial_analysis(self,column):
        df = pd.DataFrame(self.data[column].value_counts())
        df.rename(columns={"count":"real_samples"},inplace=True)
        real_probs = df/self.data.shape[0]
        df["real_probs"] = real_probs
        df["th_samples"] = multinomial.rvs(self.data.shape[0],[1/df.shape[0]]*df.shape[0],size=1)[0]
        df["th_probs"] = df["th_samples"]/self.data.shape[0]
        self.categorical_columns_stats[column]["real_samples"] = df["real_samples"].to_numpy()
        self.categorical_columns_stats[column]["real_probs"] = df["real_probs"].to_numpy()
        self.categorical_columns_stats[column]["th_multinomial_samples"] = df["th_samples"].to_numpy()
        self.categorical_columns_stats[column]["th_multinomial_probs"] = df["th_probs"].to_numpy()
        for i in range(df.shape[0]):
            self.categorical_columns_stats[column][f"{df.index[i]}_ideal_share_percentage"] = round(((df["real_samples"][df.index[i]]-df["th_samples"][df.index[i]])/df["th_samples"][df.index[i]])*100,2)

    def get_binomial_analysis(self,column):
        df = pd.DataFrame(self.data[column].value_counts())
        df.rename(columns={"count":"real_samples"},inplace=True)
        real_probs = df/self.data.shape[0]
        df["real_probs"] = real_probs
        df["th_samples"] = binom.rvs(self.data.shape[0],0.5,size=1)
        df["th_probs"] = df["th_samples"]/self.data.shape[0]
        self.categorical_columns_stats[column]["real_samples"] = df["real_samples"].to_numpy()
        self.categorical_columns_stats[column]["real_probs"] = df["real_probs"].to_numpy()
        self.categorical_columns_stats[column]["th_binom_samples"] = df["th_samples"].to_numpy()
        self.categorical_columns_stats[column]["th_binom_probs"] = df["th_probs"].to_numpy()
        self.categorical_columns_stats[column][f"{df.index[0]}_ideal_share_percentage"] = round(((df["real_samples"][df.index[0]]-df["th_samples"][df.index[0]])/df["th_samples"][df.index[0]])*100,2)
        self.categorical_columns_stats[column][f"{df.index[1]}_ideal_share_percentage"] = round(((df["real_samples"][df.index[0]]-df["th_samples"][df.index[0]])/df["th_samples"][df.index[0]])*100,2)
    
    def get_categorical_analysis(self):
        self.categorical_columns_stats = {}
        max_mode = 1
        for column in self.categorical_columns:
            self.categorical_columns_stats[column] = {}
            self.categorical_columns_stats[column]["Mode"] = self.data[column].mode().values[0]
            if max_mode < len(self.categorical_columns_stats[column]["Mode"]):
                max_mode = len(self.categorical_columns_stats[column]["Mode"])
            self.categorical_columns_stats[column]["Cardinality"] = self.data[column].dropna().unique().shape[0]
            self.get_adv_stats_categorical(column)
        print(f"Basic Stats for Categorical Columns")
        # for column in categorical_columns:
        #     len_ = len(categorical_columns_stats[column]["Mode"])
        #     if len_<max_mode:
        #         categorical_columns_stats[column]["Mode"] = categorical_columns_stats[column]["Mode"].to_list().extend([np.nan]*(max_mode-len_))
        # print(categorical_columns_stats)
        self.categorical_stats_df = pd.DataFrame(self.categorical_columns_stats)
        print(self.categorical_stats_df.applymap(lambda x:f"{x}" if type(x)==np.ndarray else x).to_markdown())

    def get_numerical_outliers(self,column):
        Q1 = self.numerical_columns_stats[column]["quartile-25"]
        Q3 = self.numerical_columns_stats[column]["quartile-75"]
        IQR = Q3 - Q1
        if (abs(self.numerical_columns_stats[column]["Mean"]-self.numerical_columns_stats[column]["std"])/self.numerical_columns_stats[column]["Mean"])*100 <= 50:
            portion = 1.5
        else:
            portion = 3
        lower_fence = Q1 - portion * IQR
        upper_fence = Q3 + portion * IQR
        outliers = self.data[(self.data[column] < lower_fence) | (self.data[column] > upper_fence)][column]
        self.numerical_columns_stats[column]["outliers_indices"] = np.array(outliers.index)
        self.numerical_columns_stats[column]["outliers_values"] = np.array(outliers.values)
    
    def analyze(self):
        
        self.get_basic_details()
        self.get_numerical_analysis()
        self.get_categorical_analysis()

        # self.basic_stats_df.to_csv("basic_stats.csv")
        excelwriter = pd.ExcelWriter(os.path.join(self.out_dir,"DataAnalysis.xlsx"),engine="openpyxl")
        self.basic_stats_df.to_excel(excelwriter,sheet_name="BasicStats")
        self.numerical_stats_df.T.to_excel(excelwriter,sheet_name="NumericalColumnStats")
        self.categorical_stats_df.T.to_excel(excelwriter,sheet_name="CategoricalColumnStats")
        excelwriter.close()

        self.get_datetime_columns()
        # html = ""
        # html += "<html>"
        # html += "<h1> Basic Details </h1>"
        # html += "TD"
        # html += "</html>"

        # with open("DataAnalysis.html","w") as f:
        #     f.write(html)

        # No of missing rows

    def get_datetime_columns(self):
        self.datetime_columns = []
        for column in self.data.columns:
            try:
                temp = pd.to_datetime(self.data[column].head(5))
                try:
                    temp = self.data[column].astype('float64')
                except Exception as e:
                    self.datetime_columns.append(column)
            except Exception as e:
                continue