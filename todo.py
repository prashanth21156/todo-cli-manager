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


def complete_task(tasks):
    """Mark a selected task as completed."""
    if not tasks:
        print("\nNo tasks found.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to complete: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[task_number - 1]

    if task.completed:
        print("Task is already completed.")
        return

    task.mark_completed()
    print("Task marked as completed!")


def remove_task(tasks):
    """Remove a selected task from the task list."""
    if not tasks:
        print("\nNo tasks found.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to remove: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    removed_task = tasks.pop(task_number - 1)
    print(f"Task '{removed_task.title}' removed successfully!")


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
            complete_task(tasks)

        elif choice == "4":
            remove_task(tasks)

        elif choice == "5":
            print("Thank you for using the To-Do List Manager!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()