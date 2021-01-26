import json
import pathlib
from datetime import date

# Functions
def create_account(username, password, firstname, lastname, emailaddress):
    username_to_db(username)
    password_to_db(password, username)
    firstname_to_db(firstname, username)
    lastname_to_db(lastname, username)
    email_to_db(emailaddress, username)
    return print("Account has been created!")

def username_to_db(username_output): 
    username_db[username_output] = {}
    todays_date = date.today()
    username_db[username_output]['Account Creation Date'] = str(todays_date)
    output_db_to_file(username_db)
    

def password_to_db(password_output, username_input): 
    username_db[username_input]['Password'] = password_output
    todays_date = str(date.today())
    username_db[username_input]['Password Creation Date'] = str(todays_date)
    output_db_to_file(username_db)

def firstname_to_db(firstname_input, username_input): 
    username_db[username_input]['FirstName'] = firstname_input
    output_db_to_file(username_db)

def lastname_to_db(lastname_output, username_input):
    username_db[username_input]['LastName'] = lastname_output
    output_db_to_file(username_db)

def email_to_db(email_address_output, username_input): 
    username_db[username_input]['Email_Address'] = email_address_output
    output_db_to_file(username_db)


def output_db_to_file(un_dict): # Write Dictionary Memory to file
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
    
    
# Variables

username_db = load_userdb()