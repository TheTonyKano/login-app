#This project is a basic login system for an application
#The goals is to have a way for the user to type in their username and then password.
#If the user does not have an account. Add an option to create an account and ask for their firstname, lastname, username, password, verification password, and email address.



#Imports

import time



#Variables

username_db = {}
main_input = ""
username = ""
username_output = ""
password_count = 0
password_attempts = 3
password_output = ""
firstname_output = ""
lastname_output = ""
email_address_output = ""



#Add to dictionary

def add_username_to_db():
    global username_output
    username_db[username_output] = {}
    
    
def add_password_to_db():
    global password_output
    username_db[username_output]['Password'] = password_output
    
    
def add_firstname_to_db():
    global firstname_output
    username_db[username_output]['FirstName'] = firstname_output
    
    
def add_lastname_to_db():
    global lastname_output
    username_db[username_output]['LastName'] = lastname_output
    
    
def add_email_to_db():
    global email_address_output
    username_db[username_output]['Email_Address'] = email_address_output
    
# Testing    
#Output Dictionary to file
def output_username_db_to_file():
    print(username_db)
    
# Testing
#Retrieve Dictionary from file
def retrieve_username_db_from_file():
    print(username_db)
    

#Main Menu and Selection Menu

def main_menu():
    #To reference to initiate restart of script
    while True:
        selection_menu()
        if main_input == "1" :
            create_account()
            continue
        elif main_input == "2":
            db_username_check()
            break
        else:
            while True:
                if main_input == "1":
                    create_account()
                elif main_input == "2":
                    db_username_check()
                    break
                else:
                    selection_menu_incorrect()
                    continue
            break

            
            
def selection_menu():
    global main_input
    print("---------------------------------------------------------")
    print("Please choose from the selection below.")
    print("1 - Create an Account")
    print("2 - Login with an Existing Account.")
    print("---------------------------------------------------------")
    main_input = input("Please type one of the numbers from above to continue:")
    return main_input


def selection_menu_incorrect():
    global main_input
    print("---------------------------------------------------------")
    print("Incorrect selection, please try again")
    print("Please choose from the selection below.")
    print("1 - Create an Account")
    print("2 - Login with an Existing Account.")
    print("---------------------------------------------------------")
    main_input = input("Type Create or Login: ")
    return main_input


#Login Menu Selection Menu

def login_menu():
   print("Please follow the prompt below to login to the application.")



#Create account functions

def create_account():
    create_username_section()
    create_password_section()
    enter_first_name()
    enter_last_name()
    enter_email_address()
    print("Your account has been created.")
    main_menu()
    
    
def create_username_section():
    while True:
        # Queue up usernames in directory for reference
        username_input = input("Enter a username you would like to use: ")
        username_list = list(username_db)
        global username_output
        username_output = username_input
        if username_input in username_list:
            print("The username you have selected is currently in use. Please try again:")
            continue
        else:
            print("Username is available. Please create a password to use.")
            add_username_to_db()
            return username_output
        
        
def create_password_section():
    # Create Password
    create_password = input("Enter password: ")
    verify_password = input("Enter password to verify: ")
    while True:
        # If the first password equals the second password display that the password matches then continue to the next part
        if create_password == verify_password:
            global password_output
            password_output = create_password
            add_password_to_db()
            print("Password matches")
            return password_output
        else:
            # If the passwords do not match, have the user retry until password matches
            print("Password does not match. Please retry")
            c_password = input("Enter password: ")
            create_password = c_password
            v_password = input("Enter password to verify: ")
            verify_password = v_password
        continue
        
        
       
def enter_email_address():
    global email_address_output
    email_address = input("Please enter your email address: ")
    email_address_verification = input("Please re-enter your email address: ")
    if email_address == email_address_verification:
        print("E-mail Addresses are matched.")
        email_address_output = email_address
        add_email_to_db()
    else:
        print("E-mail Addresses are not matching. Please re-enter your email address.")
        enter_email_address()
        
        
def enter_first_name():
    global firstname_output
    firstname_input = input("Please type your First Name:")
    firstname_output = firstname_input
    add_firstname_to_db()
    #print(firstname_output)
    return firstname_output


def enter_last_name():
    global lastname_output
    lastname_input = input("Please type your Last Name:")
    lastname_output = lastname_input
    add_lastname_to_db()
    #print(lastname_output)
    return lastname_output



# Login Functions

def db_username_check():
    login_menu()
    global username
    username = str(input("Please enter your username: "))
    # This will check if username is in Database, else it will loop until user inputs correct username.
    if username in username_db:
        # This will now ask for user's password and compare it to the account in Database
        return username, db_password_check()
    elif username == "exit" or username == "Exit":
        main_menu()
    else:
        print("The username you have entered is incorrect")
        db_username_check()
        
        
def db_password_check():
    login_menu()
    while True:
        global username
        global username_db
        user_password = input("Please enter your password:")
        userinfo_grab = username_db.get(username)
        password_grab = userinfo_grab.get('Password')
        if user_password == password_grab:
            logged_in()
            break
        else:
            print("Incorrect Password")
            global password_count
            password_count += 1
            if password_count == password_attempts :
                print("Too many attempts detected")
                time.sleep(30)
                db_username_check()
            else:
                print("")
            continue



def logged_in():
    print("You have logged in")



#----------------------------------------
#Script Starts here
#----------------------------------------
main_menu()

#User has access and now can begin to access other components of the application
