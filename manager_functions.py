# Cap Stone COMPETENCY TRACKING TOOL

import hashlib
import datetime
from competency_tracker_database import cursor



def show_manager_menu():
    prompt = """Manager Menu
(1) View All Users
(2) Search For User By First Or Last Name
(3) View Competency Report For All Users 
(4) View Competency Reports For A User 
(5) View A List Of Assessments For A User
(6) Add A User
(7) Add A New Competency
(8) Add An Assessment Result For A User 
(9) Edit A User's Information
(10) Edit A Competency
(11) Edit An Assessment 
(12) Edit An Assessment result
(13) Delete An Assessment Result
(14) Exit
    """
    prompt_choice = input(prompt)
    if prompt_choice == "1":
        view_all_users()
    elif prompt_choice == "2":
        search_user_first_name_last_name()
    elif prompt_choice == "3":
        view_comp_report_all_users()
    elif prompt_choice == "4":
        view_comp_report_a_user()
    elif prompt_choice == "5":
        view_list_of_assessment_for_a_user()
    elif prompt_choice == "6":
        add_user()
    elif prompt_choice == "7":
        add_new_competency()
    elif prompt_choice == "8":
        add_assessment_result_for_user()
    elif prompt_choice == "9":
        edit_user_info()
    elif prompt_choice == "10":
        edit_a_competency()
    elif prompt_choice == "11":
        edit_an_assesment()
    elif prompt_choice == "12":
        edit_an_assessment_result()
    elif prompt_choice == "13":
        delete_an_assessment_result()
    elif prompt_choice == "14":
        exit()



        
def view_all_users():
    select_sql= "SELECT * FROM Users"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print_user_rows(rows)

def print_user_rows(user_rows):
    print(f"{'ID':<4}{'First Name':<15}{'Last Name':<16}{'Email':<25}{'Phone':<20}{'Password':<20}{'Date Created':<20}{'Hire Date':<20}{'User Type':<8}{'Active':<4}")
    for user_row in user_rows:
        print_user_row(user_row)
        
def print_user_row(row):
    user_id = row[0] if row[0] is not None else''
    first_name = row[1] if row[1] is not None else''
    last_name = row[2] if row[2] is not None else''
    email = row[3] if row[3] is not None else''
    phone = row[4] if row[4] is not None else''
    password_hash = row[5] if row[5] is not None else''
    date_created = row[6] if row[6] is not None else''
    hire_date = row[7] if row[7] is not None else''
    user_type = row[8] if row[8] is not None else''
    active = row[9] if row[9] is not None else''
    print(f"{user_id:<4}{first_name:<15}{last_name:<16}{email:<25}{phone:<20}{password_hash:<20}{date_created:<20}{hire_date:<20}{user_type:<8}{active:<4}")
    

def search_user_first_name_last_name():
    query = input("Enter the query: ")
    select_sql= "SELECT * FROM Users where first_name like %?% or last_name like %?%"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print_user_rows(rows)

def view_comp_report_all_users():
    pass
def view_comp_report_a_user():
    pass
def view_list_of_assessment_for_a_user():
    pass

def add_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    password = input("Create Password: ")
    password_hash = hashlib.md5(password.encode())
    date_created = datetime.datetime.now()
    hire_date = input("Enter hire date: ")
    yes_no = input("Is this a manager? Y/N").lower()
    user_type = "user"
    if ("y" in yes_no):
        user_type = "manager"
    active = 1

    values = (first_name,last_name,email,phone,password_hash,date_created,hire_date,user_type,active)
    insert_into_sql = "INSERT INTO users (first_name,last_name,email,phone,password_hash,date_created,hire_date,user_type,active) VALUES(?,?,?,?,?,?,?,?,?);"
    cursor.execute(insert_into_sql,values)
    connection.commit()
    
    return print("User Added")

def add_new_competency():
    pass

def add_assessment_result_for_user():
    pass

def edit_user_info():
    pass

def edit_a_competency():
    pass

def edit_an_assesment():
    pass

def edit_an_assessment_result():
    pass

def delete_an_assessment_result():
    pass

def exit():
    pass





    

def search_users():
    query = input("Enter the query: ")
    select_sql= "SELECT * FROM Users where first_name like %?% or last_name like %?%"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print_user_rows(rows)


def edit_user():
    user_id = int(input("Enter the ID of the user you want to update: "))
    select_sql = "SELECT * FROM Users WHERE user_id = ?"
    to_update = ("first_name","last_name","email","phone","password","date_created","hire_date","user_type","active")

    cursor.execute(select_sql)
    user_row = cursor.fetchone()
    print_user_rows([user_row])

    # for num, field in enumerate(to_update):
    #     print(f'{num}: {field}')

    # field_index = int(input('\n')) + 1
    # new_value = input("What would you like the new value to be? ")
    # user_row[field_index] = new_value
    
    # # * edit_options():
    # #         * edit a user's information
    # #         * edit a competency
    # #         * edit an assessment
    # #         * edit an assessment result

    # update_user((new_value,user_id), to_update[int(user_choice)])
    # print('Your update was successful. ')
    # print(search_name(cust_name))
    # input('press enter to continue. ')






def delete_user():
    user_id = int(input('Enter the user ID:  '))
    confirm = input("Are you sure? This is PERMANENT!:")
    if (confirm == 'yes' or confirm == 'y'):
         delete_user(id)
        
    input('Customer successfully deleted!  (press enter to continue. )')


def expot_import_csv():
    pass





def competency_levels():
    pass

    # 0 = "No competency - Needs Training and Direction"   
    # 1 = "Basic Competency - Needs Ongoing Support"    
    # 2 = "Intermediate Competency - Needs Occasional Support"   
    # 3 = "Advanced Competency - Completes Task Independently"    
    # 4 = "Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations"


def view_competency_report():
    pass
