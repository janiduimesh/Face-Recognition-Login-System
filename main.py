# main.py
from modules.database import create_table
from register import register_user
from login import login

def main():
    create_table()
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()