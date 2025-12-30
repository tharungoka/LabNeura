
from config import DEPTS, YEARS, SEMS
from libs import json

# LMS = {} # GLOBAL SCOPE
# LMS["ADMINS"] = [{"name":"THARUN","password":"Tharun123"}]

with open("/Users/gtk/GTK/Innomatics-448/LMS/assets/LMS.json") as f:
    LMS = json.load(f)

def write_out():
    with open("/Users/gtk/GTK/Innomatics-448/LMS/assets/LMS.json","w") as f:
        json.dump(LMS,f,indent=4)

        
# def initialize_data():
#     # LMS = {} # LOCAL SCOPE
#     LMS["STUDENTS"] = {}
#     LMS["TEACHERS"] = {}
#     LMS["BOOKS"] ={}

#     for dept in DEPTS:
#         LMS["STUDENTS"][dept] = {}
#         for year in YEARS:
#             LMS["STUDENTS"][dept][year] = {}
#             for sem in SEMS:
#                 LMS["STUDENTS"][dept][year][sem] = []