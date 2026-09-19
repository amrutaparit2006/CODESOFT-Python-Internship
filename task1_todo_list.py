tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks added yet.")
        return
    print("\n--- TO-DO LIST ---")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['name']} [{status}]")

def add_task():
    name = input("Enter task: ").strip()
    if name:
        tasks.append({"name": name, "done": False})
        print("Task added successfully.")

def update_task():
    show_tasks()
    if not tasks:
        return
    try:
        n = int(input("Enter task number to update: "))
        if 1 <= n <= len(tasks):
            new_name = input("Enter new task: ").strip()
            if new_name:
                tasks[n-1]["name"] = new_name
                print("Task updated successfully.")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        n = int(input("Enter task number to delete: "))
        if 1 <= n <= len(tasks):
            tasks.pop(n-1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    show_tasks()
    if not tasks:
        return
    try:
        n = int(input("Enter task number to mark as done: "))
        if 1 <= n <= len(tasks):
            tasks[n-1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Done")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_done()
    elif choice == "6":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice. Try again.")
