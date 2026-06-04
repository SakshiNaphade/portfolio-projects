import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent = 4)

# Generate Task IDs
def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

# Add Task
def add_task():
    tasks = load_tasks()

    task = {
        "id": generate_id(tasks),
        "title": input("Enter task title: "),
        "priority": input("Enter task priority (Low, Medium, High): ").title(),
        "status": "pending",
        "due_date": input("Enter due date (YYYY-MM-DD): "),
    }

    if task["priority"] not in ["Low", "Medium", "High"]:
        print("Invalid priority.")
        return

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(task)
        print("-" * 20)

def search_tasks():
    tasks = load_tasks()
    keyword = input("Enter keyword to search: ")
    # for task in tasks:
    #     if keyword.lower() in task["title"].lower():
    #         print(task)
    #         print("-" * 20)
    found_tasks = [task for task in tasks if keyword.lower() in task["title"].lower()]
    if not found_tasks:
        print("No tasks found with that keyword.")
        return
    for task in found_tasks:
        print(task)
        print("-" * 20)

def mark_task_completed():
    tasks = load_tasks()
    try:
        task_id = int(input("Enter task ID to mark as completed: "))
    except ValueError:
        print("Invalid input. Task ID must be a number.")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            save_tasks(tasks)
            print("Task marked as completed!")
            return
    print("Task not found.")

def delete_task():
    tasks = load_tasks()
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid input. Task ID must be a number.")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return
    print("Task not found.")

def filter_tasks():
    tasks = load_tasks()

    print("Filter by:")
    print("1. High Priority")    
    print("2. Pending")
    print("3. Completed")

    choice = input("Enter your choice: ")
    if choice == "1":
        for task in tasks:
            if task["priority"].lower() == "high":
                print(task)
                print("-" * 20)
    elif choice == "2":
        for task in tasks:
            if task["status"].lower() == "pending":
                print(task)
                print("-" * 20)
    elif choice == "3":
        for task in tasks:
            if task["status"].lower() == "completed":
                print(task)
                print("-" * 20)
    else:
        print("Invalid choice.")


def update_task():
    tasks = load_tasks()

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID")
        return

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = input("New title: ")
            task["priority"] = input("New priority: ").title()
            task["due_date"] = input("New due date: ")

            save_tasks(tasks)

            print("Task updated successfully!")
            return

    print("Task not found.")


def task_statistics():
    tasks = load_tasks()

    total = len(tasks)

    pending = sum(
        1 for task in tasks
        if task["status"] == "Pending"
    )

    completed = sum(
        1 for task in tasks
        if task["status"] == "Completed"
    )

    high = sum(
        1 for task in tasks
        if task["priority"] == "High"
    )

    print(f"""
        Total Tasks      : {total}
        Pending Tasks    : {pending}
        Completed Tasks  : {completed}
        High Priority    : {high}
        """)        


def menu():
    while True:
        print("\n----- TASK MANAGER -----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Tasks")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Filter Tasks")
        print("7. Update Task")
        print("8. Task Statistics")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            search_tasks()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            filter_tasks()
        elif choice == "7":
            update_task()
        elif choice == "8":
            task_statistics()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()