import account_management
import db_management
import time

# Variables
main_menu_option_list = ["Login", "Create an Account", "Forgot Password/ Username", "Exit Main Menu"]
forgot_main_opt_lst = ["Forgot Username", "Forgot Password"]
main_user_input = ""
user_input = ""
database = db_management.username_db
# Prompts

def populate_menu(option):
    print("\n")
    for index, option in enumerate(option, 1):
        print(f"{index} - {option}")
    print("\n")
1

def selection_menu(menuList):
    print("\n" * 100)
    global main_user_input
    print("---------------------------------------------------------")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input


def selection_menu_incorrect(menuList):
    print("\n" * 100)
    global main_user_input
    print("---------------------------------------------------------")
    print("Incorrect selection, please try again")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input

# General Purpose Functions

def exit_application():
    print("End of Script")
    

def main_menu(): # Main Menu and Selection Menu
    print("\n" * 100)
    while True:
        selection_menu(main_menu_option_list)
        if main_user_input == "1":
            account_management.db_username_check(database)
            logged_in()
        elif main_user_input == "2":
            create_account()
        elif main_user_input == "3":
            selection_menu(forgot_main_opt_lst)
            if main_user_input == "1":
                account_management.forgot_password()
            elif main_user_input == "1":
                account_management.forgot_username()
            else:
                continue
        elif main_user_input == "4":
            exit_application()
        else:
            while True:
                if main_user_input == "1":
                    account_management.db_username_check()
                elif main_user_input == "2":
                    create_account()
                elif main_user_input == "3":
                    account_management.main()
                elif main_user_input == "4":
                    exit_application()
                else:
                    selection_menu_incorrect(main_menu_option_list)
            break

def create_account():
    db_management.check_db_file()
    # create_username_section()
    username_input = account_management.create_username_section(database)
    password_input = account_management.create_password_section()
    firstname_input = account_management.enter_first_name()
    lastname_input = account_management.enter_last_name()
    email_address = account_management.enter_email_address()
    db_management.create_account(username_input, password_input, firstname_input, lastname_input, email_address)
    
    print("Your account has been created.")
    time.sleep(10)
    main_menu()
    
    
# def forgot_credentials():
#    while True:
#        selection_menu(main_option_list)
#        if main_user_input == "1":
#            db_management.db_username_check()
#        elif main_user_input == "2":
#            create_account()
#        else:
#            while True:
#                if main_user_input == "1":
#                    db_management.db_username_check()
#                elif main_user_input == "2":
#                    create_account()
#                else:
#                    selection_menu_incorrect(main_option_list)
#                    continue
#            break



def logged_in():
    print("You have logged in")
    time.sleep(10)
    print("\n" * 100)
    


# ----------------------------------------
# Script Starts here
# ----------------------------------------

main_menu()

# User has access and now can begin to access other components of the application