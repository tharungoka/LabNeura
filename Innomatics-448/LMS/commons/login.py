from assets.data import LMS

def check_name_password(credentials):
    admin = credentials[0]
    name = credentials[1]
    password = credentials[2]
    if (admin["name"] == name) and (admin["password"] == password):
        return True
    else:
        return False

def admin_login():
    print("\nWelcome to ADMIN Login\n")
    name = input("\nPlease enter your name:")
    password = input("\nPlease enter your password:")
    # status = False
    # for admin in LMS["ADMINS"]:
    #     if (admin["name"] == name) and (admin["password"] == password):
    #         status = True
    #         break
    
    # if status:
    #     print("Login is Successfull.")
    # else:
    #     print("Login is unsuccessfull.")

    ### updated version
    all_admins = list(zip(LMS["ADMINS"],[name]*len(LMS["ADMINS"]),\
                          [password]*len(LMS["ADMINS"])))
    output = list(filter(check_name_password,all_admins))
    
    if output:
        status = True
        print("******ADMIN login is successfull******")
    else:
        status = False
        print("******Login is Unsuccessfull.******")
    return status

def student_login():
    pass

def teacher_login():
    pass

def login(type_of_login):
    if type_of_login == "ADMIN":
        login_status = admin_login()
    elif type_of_login == "STUDENT":
        login_status = student_login()
    elif type_of_login == "TEACHER":
        login_status = teacher_login()
    return login_status

    
