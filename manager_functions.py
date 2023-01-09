# Cap Stone COMPETENCY TRACKING TOOL
import bcrypt
import datetime
from competency_tracker_database import cursor, connection

def show_manager_menu():
    prompt = """Manager Menu
    (1) View All Users
    (2) Search For User By First Or Last Name
    (3) View Competency Report For All Users 
    (4) View Competency Reports For A User 
    (5) View A List Of Assessments For A User
    (6) Add A User
    (7) Add A New Competency
    (8) Add A New assessment
    (9) Add An Assessment Result For A User 
    (10) Edit A User's Information
    (11) Edit A Competency
    (12) Edit An Assessment 
    (13) Edit An Assessment result
    (14) Delete An Assessment Result
    (15) Delete User
    (16) Return to Menu
    (17) View all Competencies
    (18) View all Assessments
    (ENTER) to EXIT
    
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
        add_an_assessment()
    elif prompt_choice == "9":
        add_assessment_result_for_user()
    elif prompt_choice == "10":
        edit_user_info()
    elif prompt_choice == "11":
        edit_a_competency()
    elif prompt_choice == "12":
        edit_an_assesment()
    elif prompt_choice == "13":
        edit_assessment_result()
    elif prompt_choice == "14":
        delete_an_assessment_result()
    elif prompt_choice == "15":
        delete_user()
    elif prompt_choice == "16":
        show_manager_menu()
    elif prompt_choice == "17":
        view_all_competencies()
    elif prompt_choice == "18":
        view_all_assessments()
    else:
        exit()


def view_all_users():
    select_sql= "SELECT user_id, first_name, last_name, email, phone FROM Users"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    return print_user_rows(rows)

def print_user_rows(user_rows):
    print(f"{'ID':<4}{'First Name':<15}{'Last Name':<16}{'Email':<25}{'Phone':<20}")
    for user_row in user_rows:
        print_user_row(user_row)

def print_user_row(row):
    user_id = row[0] if row[0] is not None else''
    first_name = row[1] if row[1] is not None else''
    last_name = row[2] if row[2] is not None else''
    email = row[3] if row[3] is not None else''
    phone = row[4] if row[4] is not None else''
    print(f"{user_id:<4}{first_name:<15}{last_name:<16}{email:<25}{phone:<20}")
    show_manager_menu()
    

    
def search_user_first_name_last_name():
    query = input("Enter the Users first or last name: ")
    select_sql= "SELECT user_id, first_name, last_name, phone, email FROM Users WHERE first_name LIKE ('%' || ? || '%') OR last_name LIKE ('%' || ? || '%')"
    cursor.execute(select_sql, (query, query,))
    rows = cursor.fetchall()
    print_user_rows(rows)
    show_manager_menu()


def view_all_competencies():
    sql_statement = "SELECT competency_id, name FROM Competencies"
    competencies = cursor.execute(sql_statement).fetchall()
    print(f'{"Comp ID":<16} {"Name"}')
    for comp in competencies:
        print(f'{comp[0]:<16} {comp[1]}')



def view_comp_report_all_users():
    select_sql= "SELECT competency_id, name, date_created FROM Competencies"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print_user_rows(rows)
    show_manager_menu()
    

def print_comp_report_rows(comp_report_rows):
    print(f"{'ID':<4}{'Name':<15}{'Date Created':<16}")
    for comp_report_row in comp_report_rows:
        print_comp_report_rows(comp_report_row)
    show_manager_menu()
       

def print_comp_report_row(row):
    competency_id = row[0] if row[0] is not None else''
    name = row[1] if row[1] is not None else''
    date_created = row[2] if row[2] is not None else''
    print(f"{competency_id:<4}{name:<15}{date_created:<16}")
    show_manager_menu()


def view_comp_report_a_user():
    view_comp_report = int(input("Enter Competency ID: ")) 
    select_sql= "SELECT * From Competencies Where (competency_id) VALUES(?,?)"
    cursor.execute(select_sql,view_comp_report)
    rows = cursor.fetchall()
    print_comp_report_rows(rows)
    show_manager_menu()
    

def print_comp_report_single_user_rows(comp_report_rows):
    print(f"{'ID':<4}{'Name':<15}{'Date Created':<16}")
    for comp_report_row in comp_report_rows:
        print_comp_report_single_user_rows(comp_report_row)
       
def print_comp_report_single_user_row(row):
    competency_id = row[0] if row[0] is not None else''
    name = row[1] if row[1] is not None else''
    date_created = row[2] if row[2] is not None else''
    print(f"{competency_id:<4}{name:<15}{date_created:<16}")
   

def view_list_of_assessment_for_a_user():
    view_assessment = int(input("Enter Competency ID: ")) 
    select_sql= "SELECT * From Assessments Where (assessment_id) VALUES(?,?)"
    cursor.execute(select_sql,view_assessment)
    rows = cursor.fetchall()
    print_comp_report_rows(rows)
    show_manager_menu()
    

def print_assessmentt_single_user_rows(assessment_rows):
    print(f"{'ID':<4}{'Name':<15}{'Date Created':<16}")
    for assessment_row in assessment_rows:
        print_assessmentt_single_user_rows(assessment_row)
       
def print_comp_report_single_user_row(row):
    competency_id = row[0] if row[0] is not None else''
    name = row[1] if row[1] is not None else''
    date_created = row[2] if row[2] is not None else''
    print(f"{competency_id:<4}{name:<15}{date_created:<16}")


def add_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    password = input("Create password: ")
    password_hash = pass_hash(password)
    date_created = datetime.datetime.now()
    hire_date = input("Enter hire date: ")
    yes_no = input("Is this a manager? Y/N").lower()
    user_type = "user"
    if ("y" in yes_no):
        user_type = "manager"
    
    active = 1
    values = (first_name,last_name,email,phone,password_hash,date_created,hire_date,user_type,active)
    insert_into_sql = "INSERT INTO Users (first_name,last_name,email,phone,password_hash,date_created,hire_date,user_type) VALUES(?,?,?,?,?,?,?,?)"
    cursor.execute(insert_into_sql,values)
    connection.commit()
    print("User Added")
    show_manager_menu()
    


def pass_hash(password):
    salt = bcrypt.gensalt()
    bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(bytes, salt)
    return hashed

def add_new_competency():
    name = input("Enter name: ")
    date_created = input("Enter date created: ")
    values = (name,date_created,)
    insert_into_sql = "INSERT INTO Competencies (name,date_created) VALUES(?,?)"
    cursor.execute(insert_into_sql,values)
    connection.commit()
    print("Competency Added")
    show_manager_menu()

def add_an_assessment():
    view_all_competencies()
    competency = input("Choose the competency ID associated with the assessment: ")
    assessment_name = input("Enter a name for this assessment: ")
    date_created = datetime.date.today()
    sql_statement = "INSERT INTO Assessments (competency_id, name, date_created) VALUES (?, ?, ?)"
    values = competency, assessment_name, date_created
    cursor.execute(sql_statement, values)
    connection.commit()
    print("Assessment Created")
    show_manager_menu()


def add_assessment_result_for_user():
    view_all_competencies()
    # competency = input("Choose a Competency ID to view assessments for that competency: ")

    view_all_assessments()
    assessment = input("Choose an assessment ID to give score: ")
    user_id = input("Enter User ID to update: ")
    score = input("Enter score: ")
    date_taken = input("Enter date taken: ")
    manager_id = "1"
    sql_statement = "SELECT competency_id FROM Assessments WHERE assessment_id = ?"
    comp_id = cursor.execute(sql_statement, (assessment,)).fetchone()
    second_sql = "INSERT INTO Assessment_Results (assessment_id,user_id,competency_id,score,date_taken, manager_id) VALUES (?,?,?,?,?,?)"
    values = assessment, user_id, comp_id[0], score, date_taken, manager_id

    cursor.execute(second_sql,values)
    connection.commit()
    print("Competency Added")    
    show_manager_menu()

def edit_user_info():
    user_id = int(input("Enter the ID of the user you want to update: "))
    first_name = input("Update name: ")
    last_name = input("Update last name: ")
    email = input("Update email: ")
    phone = input("Update phone number: ")
    to_update = (first_name,last_name,email,phone,user_id)
    update_sql = "UPDATE Users SET (first_name,last_name,email,phone) WHERE (user_id) VALUES(?,?,?,?,?)"
    cursor.execute(update_sql,to_update)
    connection.commit()
    user_row = cursor.fetchone()
    print_user_rows([user_row])
    show_manager_menu()
    

def edit_a_competency():
    view_all_competencies()
    competency_id = input("Enter Competency ID to edit: ")
    name = input("Edit name: ")
    to_update = (name,competency_id)
    update_sql = "UPDATE Competencies SET name = ? WHERE competency_id = ?"
    cursor.execute(update_sql,to_update)
    connection.commit()
    show_manager_menu()


def edit_an_assesment():
    view_all_assessments()
    assessment_id = input("Enter Competency ID to edit: ")
    name = input("Edit name: ")
    to_update = (name,assessment_id)
    update_sql = "UPDATE Assessments SET name = ? WHERE assessment_id = ?"
    cursor.execute(update_sql,to_update)
    connection.commit()
    print("Successfully Edited")
    show_manager_menu()

def view_all_assessments():
    sql_statement = "SELECT * FROM Assessments"
    cursor.execute(sql_statement)
    assessments = cursor.fetchall()
    print(f"{'A ID':<10}{'C ID':<10}{'Name':<25}{'Date Created':<25}")
    for assessment in assessments:
        print(f"{assessment[0]:<10}{assessment[1]:<10}{assessment[2]:<25}{assessment[3]:<25}")
  
def edit_assessment_result():
    assessment_id = input("Enter Competency ID to edit: ")
    name = input("Edit name: ")
    to_update = (name,assessment_id)
    update_sql = "UPDATE Assessments SET (name) WHERE (assessmesnt_id) Values(?,?)"
    cursor.execute(update_sql,to_update)
    connection.commit()
    user_row = cursor.fetchone()
    print_user_rows([user_row])
    show_manager_menu()


def delete_an_assessment_result():
    assessment_id = int(input('Enter Assessment ID:  '))
    confirm = input("Are you sure? This is PERMANENT! Y/N: ").lower()
    
    if (confirm == 'yes'):
         delete_user()
    
    delete_from_sql = "DELETE * FROM Assessments WHERE assessment_id = ?"
    to_delete = (assessment_id)
    cursor.execute(delete_from_sql,to_delete)
    connection.commit()
    print('Assessment successfully deleted!')
    show_manager_menu()

def delete_user():
    user_id = int(input('Enter the user ID:  '))
    confirm = input("Are you sure? This is PERMANENT! Y/N: ").lower()
    delete_from_sql = "DELETE * FROM Users WHERE user_id = ?"
    to_delete = (user_id)
    
    if (confirm == 'yes'):
         delete_user()

    cursor.execute(delete_from_sql,to_delete)
    connection.commit()
    print('User successfully deleted!')
    show_manager_menu()
    
# 


def exit():
    while True:
        choice = input("Are you sure you want to exit? (y/n) ")
        if choice.lower() == 'y':
            print("Exiting program...")
            quit()
        elif choice.lower() == 'n':
            print("Exiting canceled.")
            show_manager_menu()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

