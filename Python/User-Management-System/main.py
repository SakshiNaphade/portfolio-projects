import json


FILE_NAME = "users.json"

def load_users():
    # Code to load users from a file or database
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    # Code to save users to a file or database
    with open(FILE_NAME, 'w') as file:
        json.dump(users, file, indent=4)    

def add_user():
    users = load_users()

    name = input("Enter name: ")
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Age must be a number.")
        return
    
    if age <= 0:
        print("Invalid age")
        return
    email = input("Enter email: ")

    for user in users:
        if user["email"] == email:
            print("User already exists!")
            return

    user = {
        "name": name,
        "age": age,
        "email": email
        }
    
    users.append(user)
    save_users(users)

    print("User added successfully!")


def view_users():
    users = load_users()
    users.sort(key=lambda user: user["name"])
    if not users:
        print("No users found.")
        return
    for user in users:
        print(user)


def search_user():
    users = load_users()
    name = input("Enter name to search: ")

    for user in users:
        if user["name"].lower() == name.lower():
            print(f"""
                Name  : {user['name']}
                Age   : {user['age']}
                Email : {user['email']}
                """)
            return
    print("User not found.")





def update_user():
    users = load_users()
    name = input("Enter name to update: ")

    for user in users:
        if user["name"].lower() == name.lower():

            user["name"] = input("Enter new name: ")
            try:
                user["age"] = int(input("Enter new age: "))
            except ValueError:
                print("Age must be a number.")
                return
            
            user["email"] = input("Enter new email: ")
            if "@" not in user["email"]:
                print("Invalid email.")
                return

            save_users(users)
            print("User updated successfully!")
            return
    print("User not found.")


def delete_user():
    users = load_users()

    name = input("Enter name to delete: ")

    for user in users:
        if user["name"].lower() == name.lower():
            users.remove(user)
            save_users(users)
            print("User deleted successfully!")
            return
    print("User not found.")

def menu():

    while True:
        print("\n----- USER MANAGEMENT SYSTEM -----")
        print("1. Add User")
        print("2. View Users")
        print("3. Search User")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_user()   
        elif choice == '2':
            view_users()
        elif choice == '3':
            search_user()
        elif choice == '4':
            update_user()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

