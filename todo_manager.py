import json
from pathlib import Path

from models import Task

TASKS_FILE = Path(__file__).with_name("tasks.json")


def _next_task_id(tasks):
    """Return the next ID without reusing IDs from removed tasks."""
    return max((task.id or 0 for task in tasks), default=0) + 1


def add_task(tasks):
    """Ask the user for a task and add it to the task list."""
    title = input("Enter task description: ").strip()

    if not title:
        print("Task description cannot be empty.")
        return False

    task = Task(_next_task_id(tasks), title)
    tasks.append(task)

    print("Task added successfully!")
    return True


def view_tasks(tasks):
    """Display all tasks with their current status."""
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"{task.id}. {task.title} [{status}]")


def _find_task(tasks, task_id):
    return next((task for task in tasks if task.id == task_id), None)


def complete_task(tasks):
    """Mark a selected task as completed."""
    if not tasks:
        print("\nNo tasks found.")
        return False

    view_tasks(tasks)

    try:
        task_id = int(input("Enter task number to complete: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return False

    task = _find_task(tasks, task_id)
    if task is None:
        print("Invalid task number.")
        return False

    if task.completed:
        print("Task is already completed.")
        return False

    task.mark_completed()
    print("Task marked as completed!")
    return True


def remove_task(tasks):
    """Remove a selected task from the task list."""
    if not tasks:
        print("\nNo tasks found.")
        return False

    view_tasks(tasks)

    try:
        task_id = int(input("Enter task number to remove: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return False

    task = _find_task(tasks, task_id)
    if task is None:
        print("Invalid task number.")
        return False

    tasks.remove(task)
    print(f"Task '{task.title}' removed successfully!")
    return True


def save_tasks(tasks, file_path=TASKS_FILE):
    """Save all tasks to a JSON file."""
    with Path(file_path).open("w", encoding="utf-8") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=2)


def load_tasks(file_path=TASKS_FILE):
    """Load tasks from a JSON file, or return an empty list if it is absent."""
    try:
        with Path(file_path).open("r", encoding="utf-8") as file:
            return [Task.from_dict(data) for data in json.load(file)]
    except FileNotFoundError:
        return []
