import time
import json
import pathlib
from getpass import getpass
from datetime import date


# Variables
username_db = {}
username = ""
username_input = ""
password_count = 0
password_attempts = 3
password_timeout = 60
password_output = ""
firstname_input = ""
lastname_output = ""
email_address_output = ""
main_menu_option_list = ["Login", "Create an Account", "Forgot Password/ Username", "Exit Main Menu"]
output_to_file = username_db
main_user_input = ""
forgot_menu_option_list = ["Forgot Username", "Forgot Password"]
user_input = ""

# Prompts
def login_menu(): # Login Menu Selection Menu
    print("Please follow the prompt below to login to the application.")
    

def populate_menu(option):
    print("\n")
    for index, option in enumerate(option, 1):
        print(f"{index} - {option}")
    print("\n")


def selection_menu(menuList):
    global main_user_input
    print("---------------------------------------------------------")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input


def selection_menu_incorrect(menuList):
    global main_user_input
    print("---------------------------------------------------------")
    print("Incorrect selection, please try again")
    print("Please choose from the selection below.")
    populate_menu(menuList)
    main_user_input = input("Please type one of the numbers from above to continue:")
    print("---------------------------------------------------------")
    return main_user_input





# General Purpose Functions
def add_username_to_db(username_output): 
    username_db[username_output] = {}
    todays_date = date.today()
    username_db[username_output]['Account Creation Date'] = str(todays_date)
    

def add_password_to_db(password_output, username_input): 
    username_db[username_input]['Password'] = password_output
    todays_date = str(date.today())
    username_db[username_input]['Password Creation Date'] = str(todays_date)


def add_firstname_to_db(firstname_input, username_input): 
    username_db[username_input]['FirstName'] = firstname_input


def add_lastname_to_db(lastname_output, username_input):
    username_db[username_input]['LastName'] = lastname_output


def add_email_to_db(email_address_output, username_input): 
    username_db[username_input]['Email_Address'] = email_address_output


def output_username_db_to_file(un_dict): # Write Dictionary Memory to file
    with open('userDB.json', 'w') as temp_dict:
        json.dump(un_dict, temp_dict)
        username_db = un_dict
        return username_db 


def check_db_file(): # Retrieve Dictionary from JSON to Memory
    file_path = pathlib.Path("userDB.json")
    while True:
        if file_path.exists():
            break
        else:
            blank_dict = {} #Makes new DB if one does not exist
            with open('userDB.json', 'w') as create_file:
                json.dump(blank_dict, create_file)
        load_userdb()
        break


def load_userdb():
    check_db_file()
    with open('userDB.json', 'r') as temp_dict:
        username_db = json.load(temp_dict)
        return username_db


def exit_application():
    print("End of Script")
    

def forgot_credentials():
    while True:
        selection_menu(forgot_menu_option_list)
        if main_user_input == "1":
            db_username_check()
        elif main_user_input == "2":
            create_account()
        else:
            while True:
                if main_user_input == "1":
                    db_username_check()
                elif main_user_input == "2":
                    create_account()
                else:
                    selection_menu_incorrect(forgot_menu_option_list)
                    continue
            break



def main_menu(): # Main Menu and Selection Menu
    while True:
        selection_menu(main_menu_option_list)
        if main_user_input == "1":
            db_username_check()
        elif main_user_input == "2":
            create_account()
        elif main_user_input == "3":
            forgot_credentials()
        elif main_user_input == "4":
            exit_application()
        else:
            while True:
                if main_user_input == "1":
                    db_username_check()
                elif main_user_input == "2":
                    create_account()
                elif main_user_input == "3":
                    forgot_credentials()
                elif main_user_input == "4":
                    exit_application()
                else:
                    selection_menu_incorrect(main_menu_option_list)
            break


# Create account functions
def create_account():
    check_db_file()
    # create_username_section()
    username_input = create_username_section()
    create_password_section(username_input)
    enter_first_name(username_input)
    enter_last_name(username_input)
    enter_email_address(username_input)
    output_username_db_to_file(username_db)
    print("Your account has been created.")
    main_menu()


def create_username_section():
    while True:
        # Queue up usernames in directory for reference
        username_input = input("Username: ")
        username_list = list(load_userdb())
        if username_input in username_list:
            print("The username you have selected is currently in use. Please try again:")
            continue
        else:
            print("Username is available. Please create a password to use.")
            add_username_to_db(username_input)


def create_password_section(username_input):
    # Create Password
    create_password = getpass("Enter password: ")
    verify_password = getpass("Enter password to verify: ")
    while True:
        # If the first password equals the second password display that the password matches then
        # continue to the next part
        if create_password == verify_password:
            password_output = create_password
            print(username_input)
            print("Password matches")
            add_password_to_db(password_output, username_input)
        else:
            # If the passwords do not match, have the user retry until password matches
            print("Password does not match. Please retry")
            c_password = getpass("Enter password: ")
            create_password = c_password
            v_password = getpass("Enter password to verify: ")
            verify_password = v_password
        continue


def enter_first_name(username_input):
    firstname_input = input("Please type your First Name:")
    add_firstname_to_db(firstname_input, username_input)
    # print(firstname_output)
    return firstname_input


def enter_last_name(username_input):
    lastname_input = input("Please type your Last Name:")
    lastname_output = lastname_input
    add_lastname_to_db(lastname_output, username_input)
    # print(lastname_output)
    return lastname_output


def enter_email_address(username_input):
    email_address = input("Please enter your email address: ")
    email_address_verification = input("Please re-enter your email address: ")
    if email_address == email_address_verification:
        print("E-mail Addresses are matched.")
        email_address_output = email_address
        add_email_to_db(email_address_output, username_input)
    else:
        print("E-mail Addresses are not matching. Please re-enter your email address.")
        enter_email_address()


# Login Functions
def db_username_check():
    username_db = load_userdb()
    # print(username_db)
    login_menu()
    username_input = str(input("Please enter your username: "))
    if username_input in username_db:
        return db_password_check(username_input, username_db)
    elif username_input == "exit" or username_input == "Exit":
        main_menu()
    else:
        print("The username you have entered is incorrect")
        db_username_check()


def db_password_check(username, username_db):
    login_menu()
    while True:
        user_password = getpass("Please enter your password:")
        userinfo_grab = username_db.get(username)
        password_grab = userinfo_grab.get('Password')
        if user_password == password_grab:
            logged_in()
            break
        else:
            print("Incorrect Password")
            global password_count
            password_count += 1
            if password_count == password_attempts:
                print("Too many attempts detected")
                time.sleep(password_timeout)
                db_username_check()
            else:
                print("")
            continue


def logged_in():
    print("You have logged in")
    main_menu()


# ----------------------------------------
# Script Starts here
# ----------------------------------------

main_menu()

# User has access and now can begin to access other components of the application