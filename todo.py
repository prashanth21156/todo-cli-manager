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
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Add Task selected")
        elif choice == "2":
            print("View Tasks selected")
        elif choice == "3":
            print("Mark Task Complete selected")
        elif choice == "4":
            print("Remove Task selected")
        elif choice == "5":
            print("Thank you for using the To-Do List Manager!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()