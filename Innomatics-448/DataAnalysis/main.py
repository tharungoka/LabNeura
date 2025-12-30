import argparse
from os import stat
import sys
sys.path.append("/Users/gtk/GTK/Innomatics-448/DataAnalysis")

from utils import FileUtils
# from services.profiling.internal.inno.inno import InnoProfiler
from services.profiling import ProfileManager
from services.analyzing import AnalyzeManager
from services.manipulation import ManipulateManager

def main(input_file : str):
    pm = ProfileManager(input_file)
    if pm.data.empty:
        print("Unsuccessful")
    else:
        print("Read Data Successfully.")

    am = AnalyzeManager(pm.profiler)
    am.analyzer.analyze()

    mm = ManipulateManager(pm.profiler)
    mm.manipulator.manipulate()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Analysis")
    parser.add_argument("--input_file", help="Please provide data file", default="/Users/gtk/GTK/Innomatics-448/DataAnalysis/assets/My_Uber_Drives_2016.csv")
    parser = parser.parse_args()
    main(parser.input_file)