def show_menu():
    print("\nTask Manager")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append(task)
    print("Task added successfully.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def remove_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed task: {removed_task}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
