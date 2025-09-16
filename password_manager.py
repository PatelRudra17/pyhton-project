def signup():
    username = input("Enter new username: ")
    email = input("enter your email: ")
    password = input("Enter new password: ")
    
    
    with open("users.txt", "a") as f:
        f.write(username + "|" + email + "|" + password + "\n")
    print("Signup successful!")


def login():
    username = input("Enter username: ")
    email = input("enter your email: ")
    password = input("Enter password: ")
   
    
    with open("users.txt", "r") as f:
        users = f.readlines()

    for line in users:
        stored_user, stored_pass = line.strip().split("|")
        if stored_user == username and stored_pass == password:
            print("Login successful! Welcome,", username)
            print("your email is :", email)
            return
    print("Invalid username or password.")

open("users.txt", "a").close()   

while True:
    print("\n1. Sign Up")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

































master_pwd = input("What is the master password? ")

def view():
    with open("password.text", "r") as f:
        for line in f.readlines():
            name, pwd = line.strip().split("|")
            print("Account:", name, "| Password:", pwd)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("password.text", "a") as f:
        f.write(name + "|" + pwd + "\n")

def remove():
    account = input("Enter account name to remove: ")
    lines = []
    with open("password.text", "r") as f:
        lines = f.readlines()
    with open("password.text", "w") as f:
        for line in lines:
            if line.startswith(account + "|"):
                continue
            f.write(line)
    print("Removed", account)

def change():
    account = input("Enter account name to change password: ")
    new_pwd = input("Enter new password: ")
    updated = False
    lines = []
    with open("password.text", "r") as f:
        lines = f.readlines()
    with open("password.text", "w") as f:
        for line in lines:
            if line.startswith(account + "|"):
                f.write(account + "|" + new_pwd + "\n")
            else:
                f.write(line)

            if updated :
                print("chnaged password for", account)
            else:
                print("account not found")

            
while True:
    mod = input("What do you want to do? (view/add/remove/change), press q to quit: ")
    if mod == "q":
        break
    elif mod == "view":
        view()
    elif mod == "add":
        add()
    elif mod == "remove":
        remove()
    elif mod == "change":
        change()
    else:
        print("Invalid option")

