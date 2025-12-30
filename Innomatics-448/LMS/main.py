"""
This file is the starting file for Innomatics LMS projects
And it contains business logic of LMS.

Authors: tharunkumargoka2020@gmail.com
Copy rights: 2025@Innomatics.
"""
import sys
sys.path.append(r"/Users/gtk/GTK/Innomatics-448/LMS")

# from assets.data import initialize_data
from assets.data import write_out
from commons.login import login
from utils.admin_utils import process_request
from utils.display_utils import (
    display_admin_options,
    display_login_options,
    display_student_options,
    display_teacher_options
)

def main():
    """
    Main function is a startng point for LMS.
    """
    print("="*40)
    print("Welcome to LMS")
    print("="*40)
    # Initializing our data.
    login_status, turn_off, selected = display_login_options()
    if turn_off:
        print("Turning Off the Software")
        write_data()
        return # Successfull Return GraceFul Return
    # login_status = login()
    if login_status:
        # initialize_data()
        if selected == "ADMIN":
            choice = display_admin_options()
            process_request(choice)
        elif selected == "STUDENT":
            display_student_options()
        elif selected == "TEACHER":
            display_teacher_options()
        status = True
        while status:
            login_status, turn_off, selected = display_login_options()
            if turn_off:
                write_out()
                print("Turing Off the Software")
                status = False
    else:
        write_out()
        print("Unsuccessful Login.Exiting LMS. Please try again.")

if __name__ == "__main__":
    main()