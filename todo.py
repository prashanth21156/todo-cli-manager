class Task:
    """Represent a single to-do task."""

    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True


def display_menu():
    """Display the main menu options."""
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. Exit")


def add_task(tasks):
    """Ask the user for a task and add it to the task list."""
    title = input("Enter task description: ").strip()

    if not title:
        print("Task description cannot be empty.")
        return

    task = Task(title)
    tasks.append(task)

    print("Task added successfully!")


def view_tasks(tasks):
    """Display all tasks with their current status."""
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{index}. {task.title} [{status}]")


def main():
    """Run the main To-Do application."""
    tasks = []

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

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