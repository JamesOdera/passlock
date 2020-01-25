#!/usr/bin/env python3.6

from user import User


def create_user(fname,lname,password,email):
    '''
    Fxn to create a new user
    '''
    new_user = User(fname,lname,password,email)
    return new_user

def save_users(user):
    '''
    Fxn to save user
    '''
    user.save_users()

def del_user(user):
    '''
    Fxn to delete user
    '''
    user.delete_user()

def find_user(password):
    '''
    Fxn to find user by passwrd
    '''
    return User.find_by_password(password)

def check_existing_users(password):
    '''
    Fxn to check if user exist
    '''
    return User.user_exist(password)

def display_users():
    '''
    Fxn to show saved users
    '''
    return User.display_users()


## Main function

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a user a/c, du - display users, fu -find a user, ex -exit the  list ")

        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Password ...")
            p_password = input()

            print("Email address ...")
            e_address = input()


            save_contacts(create_contact(f_name,l_name,p_password,e_address)) # create and save new contact.
            print ('\n')
            print(f"New User {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} .....{user.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any user list saved yet")
                print('\n')

        elif short_code == 'fu':
            if find_user():

                print("Enter the passwrd you want to search for")

                search_password = input()
            if check_existing_users(search_password):
                search_password = find_user(search_password)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)

                print(f"Password.......{search_user.password}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That contact does not exist")



        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

    
if __name__ == '__main__':

    main()