import json
import os

def load_users(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_users(users,filename):
    with open(filename, 'w') as file:
        json.dump(users,file)

filename = 'users.json'
users = load_users(filename)

def new_login():
    new_user = input('Create a user: ')
    new_password = ''
    while True:
        new_password = input('Create a password: ')
        if len(new_password) < 5:
            print('You password need a 5 characters')
        else:
            break
    users[new_user] = new_password
    print('Success!')
    save_users(users,filename)

def login(users):
    for i in range(3):
        user = input('Enter your user: ')
        password = input('Enter your password: ')
        if user in users and users[user] == password:
            print(f'Welcome {user}!')
            break
        else:
            print('User or password incorret, try again')
            if i == 2:
                print('Sorry multiple attempts!')

choice = int(input('Enter 1 for new user or 2 to log in: '))
if choice == 1:
    new_login()
elif choice == 2:
    login(users)