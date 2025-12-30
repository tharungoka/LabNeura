from assets.data import LMS
from utils.display_utils import (
    display_branch_details,
    display_year_details,
    display_sem_details
)
def add_student():
    status = True
    while status:
        print("="*40)
        print("STDUENT DETAILS")
        print("="*40)
        print("BRANCH DETAILS")
        branch = display_branch_details()
        print("YEAR DETAILS")
        year = display_year_details()
        print("SEM DETAILS")
        sem = display_sem_details()
        name = input("Enter student name")
        password = input("Enter password")
        student = {"name":name,"password":password}
        #Other details like rollno, address, phone no
        LMS["STUDENTS"][branch][year][sem].append(student)
        choice = input("Do you want to add one more student(Y/N)")
        if choice != "y":
            status = False
