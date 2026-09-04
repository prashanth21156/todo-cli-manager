from todo_manager import add_task, complete_task, load_tasks, remove_task, save_tasks, view_tasks


def display_menu():
    """Display the main menu options."""
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. Exit")


def main():
    """Run the main To-Do application."""
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            changed = add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
            changed = False
        elif choice == "3":
            changed = complete_task(tasks)
        elif choice == "4":
            changed = remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Thank you for using the To-Do List Manager!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            changed = False

        if changed:
            save_tasks(tasks)


if __name__ == "__main__":
    main()
