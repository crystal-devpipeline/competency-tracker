# Cap Stone COMPETENCY TRACKING TOOL

import hashlib
import manager_functions
import user_functions
from competency_tracker_database import cursor


def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    password_hash = hashlib.md5(password.encode())
    select_sql = "SELECT password_hash, user_type, user_id FROM Users WHERE email=?"
    values = (email)
    cursor.execute(select_sql, values)
    row = cursor.fetchone()
    if password_hash != row[0]:
       return print("Login Failed")
    if row[1] == "manager":
        manager_functions.show_manager_menu()
    else:
        user_functions.show_user_menu(row[2])

login()