from competency_tracker_database import cursor
from competency_tracker_database import connection

def show_user_menu(user_id):
    prompt= """User Menu
    (1) View Competency & Assessment Report
    (2) Edit User Information 
    (3) Exit
    """
    while True: 
        prompt_choice = input(prompt)

        if prompt_choice == "1":
            view_user_comp_assessment_report(user_id)
        elif prompt_choice == "2":
            edit_user_info(user_id)
        elif prompt_choice == "3":
            exit()

def view_user_comp_assessment_report(user_id):
    pass



def edit_user_info(user_id):
    select_sql = "SELECT first_name, last_name, email, phone, password_hash FROM Users WHERE user_id = ?"
    cursor.execute(select_sql, user_id)
    row = cursor.fetchone()
    print_user_row(row)

    prompt= """"Which field would you like to update? 
    (F)irst Name
    (L)ast Name
    (E)mail
    (P)hone
    P(a)ssword
    """
    while True:
        prompt_choice = input(prompt.upper())

        if prompt_choice.upper == "f":
            edit_user_info(row[0])
        elif prompt_choice == "l":
            edit_user_info(row[1])
        elif prompt_choice == "e":
            edit_user_info(row[2])
        elif prompt_choice == "p":
            edit_user_info(row[3])
        elif prompt_choice == "a":
            edit_user_info(row[4])
        else:
            print("/n Update Complete")
        



def print_user_row(user_row):
    print(f"{'First Name':<15}{'Last Name':<16}{'Email':<25}{'Phone':<20}{'Password':<20}")
    print(f"{user_row[0]:<15}{user_row[1]:<16}{user_row[2]:<25}{user_row[3]:<20}{'********'<20}")

    print_user_row()

    cursor.execute(select_sql)
    user_row = cursor.fetchone()
    print_user_rows([user_row])

    for num, field in enumerate(to_update):
        print(f'{num}: {field}')

    field_index = int(input('\n')) + 1
    new_value = input("What would you like the new value to be? ")
    user_row[field_index] = new_value




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

