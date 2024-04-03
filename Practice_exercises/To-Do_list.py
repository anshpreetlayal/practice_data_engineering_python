
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")


def view_list():
    if todo_list:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("\nThe to-do list is empty.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View the to-do list")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_list()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")