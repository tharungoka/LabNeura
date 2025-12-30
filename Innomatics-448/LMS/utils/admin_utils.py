from utils.student_utils import add_student
from utils.display_utils import display_admin_options
def process_request(choice):
    if choice == 1:
        add_student()
        display_admin_options()