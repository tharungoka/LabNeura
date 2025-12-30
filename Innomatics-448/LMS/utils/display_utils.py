from commons.login import login
from config import (
    DEPTS,
    YEARS,
    SEMS
)
def display_admin_options():
    status = True
    while(status):
        print("ADMIN MENU")
        print("1.Adding Student\n2.Adding a Book\n3.Adding a Teacher\n4.Adding Admin\n5.Logout")
        choice = input("Please enter your choice 1/2/3/4/5: ")
        if choice == "1":
            return 1
        elif choice == "2":
            print("Adding Book")
        elif choice == "3":
            print("Adding Teacher")
        elif choice == "4":
            print("Adding Admin")
        elif choice == "5":
            print("Logging out..")
            status = False
        else:
            print("Invalid input")

def display_login_options():
    status = True
    turn_off = False
    login_status = None
    selected = None
    while(status):
        print("\n")
        print("Who are you?? Select anyone below.")
        print("\n")
        print("1.ADMIN\n2.STUDENT\n3.TEACHER\n4.TURN OFF")
        print("\n")
        choice = input("Please enter your choice 1/2/3/4: ")
        if choice == "1":
            login_status = login("ADMIN")
            selected = "ADMIN"
            status = False
        elif choice == "2":
            login_status = login("STUDENT")
            selected = "STUDENT"
            status = False
        elif choice == "3":
            login_status = login("TEACHER")
            selected = "TEACHER"
            status = False
        elif choice == "4":
            print("Turn Off")
            status = False
            turn_off = True
        else:
            print("Invalid input")
    return (login_status,turn_off,selected)

def display_student_options():
    pass

def display_teacher_options():
    pass

def display_branch_details():
    status = True
    while(status):
        s_no = 1
        print("DEPARTMENT DETAILS")
        for dept in DEPTS:
            print(f"{s_no}.{dept}")
            s_no += 1
        # choice = input("SELECT any branch: ")
        # if choice == 1:
        #     return DEPTS[0]
        # elif choice == 2:
        #     return DEPTS[1]
        # elif choice == 3:
        #     return DEPTS[2]
        # elif
        status = True
        while status:
            try:
                choice = int(input("SELECT any branch: "))
                status = False
            except:
                print("Invalid Choice. Please enter numbers only..")
        if choice in range(1,len(DEPTS)+1):
            return DEPTS[choice-1]
        
def display_year_details():
    status = True
    while(status):
        s_no = 1
        print("YEAR DETAILS")
        for year in YEARS:
            print(f"{s_no}.{year}")
            s_no += 1
        choice = input("SELECT any Year: ")
        # if choice == 1:
        #     return DEPTS[0]
        # elif choice == 2:
        #     return DEPTS[1]
        # elif choice == 3:
        #     return DEPTS[2]
        # elif
        status = True
        while status:
            try:
                choice = int(choice)
                status = False
            except:
                print("Invalid Choice. Please enter numbers only..")
        if choice in range(1,len(YEARS)+1):
            return YEARS[choice-1]
        
def display_sem_details():
    status = True
    while(status):
        s_no = 1
        print("SEM DETAILS")
        for sem in SEMS:
            print(f"{s_no}.{sem}")
            s_no += 1
        choice = input("SELECT any Sem: ")
        # if choice == 1:
        #     return DEPTS[0]
        # elif choice == 2:
        #     return DEPTS[1]
        # elif choice == 3:
        #     return DEPTS[2]
        # elif
        status = True
        while status:
            try:
                choice = int(choice)
                status = False
            except:
                print("Invalid Choice. Please enter numbers only..")
        if choice in range(1,len(SEMS)+1):
            return SEMS[choice-1]