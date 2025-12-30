import numpy as np
from scipy.stats.mstats import gmean
def create_np_array(line : list):
    line_np = np.array(line)
    del line
    return line_np

def create_np_arrays(lines : list):
    np_arrays = list(map(create_np_array, lines))
    return np_arrays

def get_whole_data_summary(arr : np.ndarray):
    # numpy operations
    sum_ = np.sum(arr)
    print(f"Sum of whole data is {sum_}")
    sum_1 = np.sum(arr,axis=0)
    print(f"Sum of whole data columnwise is {sum_1}")
    sum_2 = np.sum(arr,axis=1)
    print(f"Sum of whole data rowwise is {sum_2}")
    max_ = np.max(arr)
    print(f"Max of whole data is {max_}")
    min_ = np.min(arr)
    print(f"Min of whole data is {min_}")
    mean_ = np.mean(arr)
    print(f"Mean of whole data is {mean_}") 
    median_ = np.median(arr)
    print(f"Median of the whole data is {median_}")
    
    # All arithmetic numpy functions
    # np.add
    # np.multiply
    # np.divide
    # np.subtract

    matrix_addition = np.add(arr,arr)
    matrix_subtraction = np.subtract(arr,arr)
    matrix_multiplication = np.multiply(arr,arr)
    matrix_division = np.divide(arr,arr)

    # Maths
    # np.log10
    log10 = np.log10(arr)
    sqrt = np.sqrt(arr)
    abs_ = np.abs(arr)
    sin_ = np.sin(arr)

def get_geomean(arr : np.ndarray):
    return np.prod(arr)**1/arr.size

def get_measures_ct(arr :  np.ndarray):
    # mean, median, geomean
    mean_ = np.mean(arr)
    median_ = np.median(arr)
    geomean_ = gmean(arr)
    # return (mean_, median_, geomean_) # Return by value
    return {"mean":mean_, "median":median_, "gmean":geomean_}

def get_column_summary(arr :  np.ndarray):
    column_summary = list(map(get_measures_ct, arr))
    for i in range(0, len(column_summary)):
        print(f"{i+1} column summary : {column_summary[i]}")