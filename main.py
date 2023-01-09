# Cap Stone COMPETENCY TRACKING TOOL

import bcrypt
import manager_functions
import user_functions
from competency_tracker_database import cursor

def intialize():
    option = input("(1)Login or (2)Create an account: \n")
    if option == "1" :
        return login()
    elif option == "2" :
        return manager_functions.add_user()
    # else:
    #     return option
    


def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    select_sql = "SELECT user_id, password_hash, user_type FROM Users WHERE email=?"
    values = (email,)
    fetched_user = cursor.execute(select_sql, values).fetchone()
    if fetched_user == None:
        print("Not found")
    elif bcrypt.checkpw(password.encode('utf-8'), fetched_user[1]):
        user_type = fetched_user[2]
        user_id = fetched_user[0]
        if user_type == "manager":
            print("Logged In")
            manager_functions.show_manager_menu()
        else:
            print("Logged In")
            user_functions.show_user_menu(user_id)
        
# add something so you stay logged in


    # if
    # if password_hash != row[0]:
    #    return print("Login Failed")
    # if row[1] == "manager":
    #     manager_functions.show_manager_menu()
    # else:
    #     user_functions.show_user_menu(row[2])

intialize()