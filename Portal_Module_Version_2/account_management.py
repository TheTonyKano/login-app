from getpass import getpass
import time


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



def main():
    print("")

def forgot_password():
    print("")


def forgot_username():
    print("")



        
        
# Create account functions
def create_username_section(database):
    while True:
        # Queue up usernames in directory for reference
        username_input = input("Username: ")
        database_lst = list(database)
        if username_input in database_lst:
            print("The username you have selected is currently in use. Please try again:")
            continue
        else:
            print("Username is available. Please create a password to use.")
            time.sleep(1)
            return username_input


def create_password_section():
    # Create Password
    create_password = getpass("Enter password: ")
    verify_password = getpass("Enter password to verify: ")
    while True:
        # If the first password equals the second password display that the password matches then
        # continue to the next part
        if create_password == verify_password:
            print("Password matches")
            return  create_password
        else:
            # If the passwords do not match, have the user retry until password matches
            print("Password does not match. Please retry")
            create_password = getpass("Enter password: ")
            verify_password = getpass("Enter password to verify: ")
            continue


def enter_first_name():
    firstname_input = input("Please type your First Name:")
    # print(firstname_output)
    return firstname_input


def enter_last_name():
    lastname_input = input("Please type your Last Name:")
    lastname_output = lastname_input
    # print(lastname_output)
    return lastname_output


def enter_email_address():
    email_address = input("Please enter your email address: ")
    email_address_verification = input("Please re-enter your email address: ")
    if email_address == email_address_verification:
        print("E-mail Addresses are matched.")
        return email_address
    else:
        print("E-mail Addresses are not matching. Please re-enter your email address.")
        enter_email_address()


# Login Functions
def db_username_check(database):
    database_lst = list(database)
    # print(username_db)
    username_input = str(input("Please enter your username: "))
    if username_input in database_lst:
        return db_password_check(username_input, database)
    elif username_input == "exit" or username_input == "Exit":
        return
    else:
        print("The username you have entered is incorrect")
        db_username_check()


def db_password_check(username, database):
    while True:
        user_password = getpass("Please enter your password:")
        userinfo_grab = database.get(username)
        password_grab = userinfo_grab.get('Password')
        if user_password == password_grab:
            return
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

