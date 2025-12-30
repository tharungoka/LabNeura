import sys
sys.path.append("/Users/gtk/GTK/Innomatics-448/Numpy")

import argparse
import numpy as np
from scipy.stats.mstats import gmean
from utils.os_utils import (
    check_file_status,
    read_file
)
from utils.list_utils import create_lists
from utils.type_utils import convert_all_lines
from utils.numpy_utils import (
    create_np_arrays,
    get_whole_data_summary,
    get_column_summary
)

def main():
    print("Welcome!!")
    parser = argparse.ArgumentParser(description="Help on Numpy Analyzer")
    parser.add_argument("--input_file",help="Please provide an input csv file",
                        default="/Users/gtk/GTK/Innomatics-448/Numpy/assets/numpy_random_numbers.csv",required=False)                        
    parser.add_argument("--delimeter",help="provide delimiter", default=",", required=False)
    parser = parser.parse_args()

    input_file = parser.input_file
    delimeter = parser.delimiter
    status = check_file_status(input_file)
    if status:
        print("File is available")
    else:
        print("Invalid File")

    lines = read_file(input_file)
    header_line = lines[0]
    list_lines = create_lists(lines)
    converted_lines = convert_all_lines(list_lines)
    np_arrays = create_np_arrays(converted_lines)
    whole_data = np.array(np_arrays) # 2D Array (DataFrame)
    get_whole_data_summary(whole_data)
    # Apply all operations as whole 2D, axis wise 0,1
    # Apply all statistical measures on columns
    get_column_summary(whole_data.T)
    # temp = str(whole_data.T[0]).replace(" ",",")
    # print(temp.replace(",,",","))

if __name__ == "__main__":
    main()