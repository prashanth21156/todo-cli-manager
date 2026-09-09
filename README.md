# To-Do List Manager – Python CLI Application

## Project Overview

The To-Do List Manager is a command-line application developed using Python. It allows users to create, view, complete, and remove tasks through a simple interactive menu.

The application uses a modular design by separating the user interface, task model, and task management logic into different Python files. Tasks are stored in a JSON file so that task information can be preserved between application runs.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Remove tasks
- Automatically assign task IDs
- Prevent empty task descriptions
- Validate task number input
- Prevent invalid task selection
- Prevent marking an already completed task again
- Save tasks to a JSON file
- Load previously saved tasks when the application starts
- Automated unit testing using Python `unittest`

## Technologies Used

- Python 3
- JSON
- Python `pathlib`
- Python `unittest`
- Git and GitHub

## Project Structure

```text
todo-cli-manager/
│
├── main.py
├── models.py
├── todo_manager.py
├── test_todo.py
├── README.md
├── requirements.txt
└── .gitignore
### File Description

| File | Purpose |
|---|---|
| `main.py` | Contains the main menu and controls the application flow |
| `models.py` | Defines the `Task` class and task data structure |
| `todo_manager.py` | Contains task operations and JSON persistence functions |
| `test_todo.py` | Contains automated unit tests |
| `README.md` | Project documentation |
| `requirements.txt` | Dependency file |
| `.gitignore` | Prevents unnecessary files from being tracked |
| `tasks.json` | Stores task information in JSON format |

## Application Architecture

The application follows a modular architecture:

```text
User
  |
  v
main.py
  |
  v
todo_manager.py
  |
  +-------------------+
  |                   |
  v                   v
models.py          tasks.json
  |
  v
Task Object
```

Then paste the next section:

````markdown
### Main Components

**1. main.py**

Controls the application menu and receives the user's choice.

The available options are:

1. Add Task
2. View Tasks
3. Mark Task Complete
4. Remove Task
5. Exit

**2. models.py**

Contains the `Task` class.

Each task contains:

- Task ID
- Task title
- Completion status

The `Task` class provides methods for:

- Marking a task as completed
- Converting a task into dictionary format
- Creating a task from dictionary data

**3. todo_manager.py**

Contains the main task management operations:

- `add_task()`
- `view_tasks()`
- `complete_task()`
- `remove_task()`
- `save_tasks()`
- `load_tasks()`

**4. test_todo.py**

Contains automated unit tests for:

- Task creation
- Task completion
- Adding tasks
- Removing tasks
- Converting tasks to dictionary format
- Saving and loading tasks
- Handling a missing JSON file
## Application Flow

The following flow shows how the To-Do List Manager works from starting the application to exiting it.

```text
START
  |
  v
Load tasks from tasks.json
  |
  v
Display Main Menu
  |
  v
Get User Choice
  |
  +---- 1 ----> Add Task
  |                |
  |                v
  |          Enter Task Description
  |                |
  |                v
  |          Is description empty?
  |             /       \
  |           Yes        No
  |            |          |
  |            v          v
  |       Show Error   Create Task
  |                       |
  |                       v
  |                  Save Tasks
  |
  +---- 2 ----> View Tasks
  |                |
  |                v
  |          Display Tasks
  |
  +---- 3 ----> Mark Task Complete
  |                |
  |                v
  |          Enter Task Number
  |                |
  |                v
  |          Validate Task
  |                |
  |                v
  |          Mark Completed
  |                |
  |                v
  |             Save Tasks
  |
  +---- 4 ----> Remove Task
  |                |
  |                v
  |          Enter Task Number
  |                |
  |                v
  |          Validate Task
  |                |
  |                v
  |           Remove Task
  |                |
  |                v
  |             Save Tasks
  |
  +---- 5 ----> Exit
                   |
                   v
                  END
```

### Application Flow Explanation

1. The application starts.
2. Previously saved tasks are loaded from `tasks.json`.
3. The main menu is displayed.
4. The user selects an operation.
5. The selected operation is executed.
6. If the task list is modified, the updated tasks are saved to `tasks.json`.
7. The menu is displayed again.
8. The application continues until the user selects **Exit**.
## Pseudocode

The following pseudocode describes the main logic of the application.

```text
START

Load tasks from tasks.json

REPEAT

    Display main menu

    Read user's choice

    IF choice = 1 THEN

        Ask user for task description

        IF description is empty THEN
            Display "Task description cannot be empty"
        ELSE
            Generate next task ID
            Create a new Task
            Add task to task list
            Save tasks
            Display success message
        END IF

    ELSE IF choice = 2 THEN

        IF task list is empty THEN
            Display "No tasks found"
        ELSE
            Display all tasks
            Display task status as Pending or Completed
        END IF

    ELSE IF choice = 3 THEN

        IF task list is empty THEN
            Display "No tasks found"
        ELSE
            Display all tasks
            Ask user for task number

            IF input is not a valid number THEN
                Display invalid input message
            ELSE
                Find the selected task

                IF task does not exist THEN
                    Display invalid task number
                ELSE IF task is already completed THEN
                    Display already completed message
                ELSE
                    Mark task as completed
                    Save tasks
                    Display success message
                END IF
            END IF
        END IF

    ELSE IF choice = 4 THEN

        IF task list is empty THEN
            Display "No tasks found"
        ELSE
            Display all tasks
            Ask user for task number

            IF input is not a valid number THEN
                Display invalid input message
            ELSE
                Find the selected task

                IF task does not exist THEN
                    Display invalid task number
                ELSE
                    Remove the selected task
                    Save tasks
                    Display success message
                END IF
            END IF
        END IF

    ELSE IF choice = 5 THEN

        Save tasks
        Display exit message
        STOP

    ELSE

        Display "Invalid choice"

    END IF

UNTIL user chooses Exit

END
```
## Worked Example

The following example demonstrates the complete task management process.

### 1. Adding Tasks

The user selects option `1`:

```text
===== TO-DO LIST MANAGER =====
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Remove Task
5. Exit

Enter your choice: 1
Enter task description: Learn Python
Task added successfully!
```

The application assigns Task ID `1`.

The user adds another task:

```text
Enter your choice: 1
Enter task description: Practice Git
Task added successfully!
```

The application assigns Task ID `2`.

The task list is now:

```text
1. Learn Python [Pending]
2. Practice Git [Pending]
```

### 2. Viewing Tasks

The user selects option `2`:

```text
Enter your choice: 2

===== YOUR TASKS =====
1. Learn Python [Pending]
2. Practice Git [Pending]
```

### 3. Completing a Task

The user selects option `3`:

```text
Enter your choice: 3

===== YOUR TASKS =====
1. Learn Python [Pending]
2. Practice Git [Pending]

Enter task number to complete: 1
Task marked as completed!
```

The task status changes from `Pending` to `Completed`:

```text
1. Learn Python [Completed]
2. Practice Git [Pending]
```

### 4. Removing a Task

The user selects option `4`:

```text
Enter your choice: 4

===== YOUR TASKS =====
1. Learn Python [Completed]
2. Practice Git [Pending]

Enter task number to remove: 2
Task 'Practice Git' removed successfully!
```

The final task list becomes:

```text
===== YOUR TASKS =====
1. Learn Python [Completed]
```

### 5. JSON Data Example

The completed task is stored in `tasks.json` in the following format:

```json
[
  {
    "id": 1,
    "title": "Learn Python",
    "completed": true
  }
]
```

This demonstrates how the application's task data is persisted between executions.
## Error Handling and Input Validation

The application includes input validation to prevent invalid user input from causing the program to stop unexpectedly.

### 1. Empty Task Description

If the user tries to add a task without entering a description:

```text
Enter task description:
Task description cannot be empty.
```

The task is not added.

### 2. Invalid Menu Choice

If the user enters a menu option outside the range `1–5`:

```text
Enter your choice: 8
Invalid choice. Please enter a number from 1 to 5.
```

The application returns to the main menu.

### 3. Non-Numeric Task Number

If the user enters text instead of a task number:

```text
Enter task number to complete: abc
Invalid input. Please enter a valid task number.
```

The application continues running without crashing.

### 4. Invalid Task Number

If the user enters a task number that does not exist:

```text
Enter task number to remove: 99
Invalid task number.
```

No task is removed.

### 5. Already Completed Task

If the user tries to complete a task that is already completed:

```text
Task is already completed.
```

The task remains unchanged.

### 6. Empty Task List

If there are no tasks and the user selects an operation such as View, Complete, or Remove:

```text
No tasks found.
```

The application safely returns to the main menu.

### Error Handling Summary

| Input/Condition | Application Response |
|---|---|
| Empty task description | Displays an error and does not add the task |
| Invalid menu choice | Displays an error and returns to menu |
| Non-numeric task number | Displays an error without crashing |
| Non-existent task number | Displays invalid task number |
| Already completed task | Displays an informational message |
| Empty task list | Displays "No tasks found." |
## Data Persistence

The application uses a JSON file named `tasks.json` to store task information permanently.

The persistence functionality is implemented using two functions in `todo_manager.py`:

- `save_tasks()` – saves the current task list to `tasks.json`.
- `load_tasks()` – loads previously saved tasks when the application starts.

### Saving Tasks

When a task is added, completed, or removed, the application saves the updated task list.

Example:

```text
Task List
1. Learn Python [Completed]
2. Practice Git [Pending]
```

The corresponding JSON data is:

```json
[
  {
    "id": 1,
    "title": "Learn Python",
    "completed": true
  },
  {
    "id": 2,
    "title": "Practice Git",
    "completed": false
  }
]
```

### Loading Tasks

When the application starts, `main.py` calls:

```text
load_tasks()
```

The program reads `tasks.json` and converts the stored JSON data back into `Task` objects.

The process is:

```text
Start Application
       |
       v
load_tasks()
       |
       v
Read tasks.json
       |
       v
Convert JSON data into Task objects
       |
       v
Display Main Menu
```

### Missing JSON File

If `tasks.json` does not exist, the `load_tasks()` function handles the `FileNotFoundError` and starts with an empty task list.

```text
tasks.json not found
       |
       v
FileNotFoundError handled
       |
       v
Return empty task list
       |
       v
Application continues normally
```

This prevents the application from crashing when it is run for the first time.
## Testing

Automated testing is implemented using Python's built-in `unittest` framework.

The test suite contains **7 test cases** covering task creation, completion, task-list operations, and JSON persistence.

### Test Cases

| Test Case | Purpose |
|---|---|
| `test_task_creation` | Verifies that a task is created with the correct ID, title, and status |
| `test_mark_completed` | Verifies that a task can be marked as completed |
| `test_add_task` | Verifies that a task can be added to the task list |
| `test_remove_task` | Verifies that a task can be removed from the task list |
| `test_task_to_dict` | Verifies conversion of a Task object to dictionary format |
| `test_save_and_load_tasks` | Verifies saving and loading tasks using JSON |
| `test_load_missing_file_returns_empty_list` | Verifies that a missing JSON file is handled safely |

### Running the Tests

The tests can be executed using:

```powershell
python -m unittest test_todo.py
```

The complete test suite can also be executed using:

```powershell
python -m unittest discover
```

### Expected Testing Result

```text
.......
----------------------------------------------------------------------
Ran 7 tests

OK
```

A successful `OK` result indicates that all 7 automated test cases passed without failures.

### Testing Coverage

The tests verify the following major areas:

- Task object creation
- Task completion
- Task list addition
- Task removal
- JSON serialization
- JSON save and load operations
- Missing file handling
## How to Run the Application

### Prerequisites

Python 3 must be installed on the system.

No external Python packages are required because the application uses Python's standard library.

### Run the Application

Open the terminal in the project directory and execute:

```powershell
python main.py
```

The application will display the main menu:

```text
===== TO-DO LIST MANAGER =====
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Remove Task
5. Exit
```

Enter the number corresponding to the operation you want to perform.

### Run the Automated Tests

To run the tests:

```powershell
python -m unittest test_todo.py
```

To discover and run all tests:

```powershell
python -m unittest discover
```

## Design Choices

### Modular Design

The application is divided into separate modules based on responsibility.

- `main.py` manages the user interface and application flow.
- `models.py` defines the `Task` class.
- `todo_manager.py` contains task operations and data persistence.
- `test_todo.py` contains automated tests.

This separation makes the application easier to understand, maintain, test, and extend.

### Object-Oriented Task Model

A `Task` class is used to represent individual tasks.

Each task contains:

- ID
- Title
- Completion status

This provides a structured way to manage task information.

### JSON Storage

JSON was selected for data persistence because it is simple, human-readable, and supported by Python's standard library.

### Automatic Task IDs

The application automatically generates task IDs using the highest existing ID plus one.

This also prevents IDs from being reused after a task is removed.

### Standard Python Libraries

The project does not require external dependencies. It uses built-in modules such as:

- `json`
- `pathlib`
- `unittest`

## Project Statistics

| Metric | Value |
|---|---:|
| Python source modules | 3 |
| Test file | 1 |
| Core task operations | 4 |
| Automated test cases | 7 |
| Data storage format | JSON |
| External dependencies | 0 |
| Main application file | `main.py` |
| Task model file | `models.py` |
| Task management file | `todo_manager.py` |

## Project Deliverables

The completed project contains:

1. `main.py` - Main CLI application
2. `models.py` - Task data model
3. `todo_manager.py` - Task management and persistence logic
4. `test_todo.py` - Automated unit tests
5. `README.md` - Complete project documentation
6. `requirements.txt` - Dependency information
7. `.gitignore` - Git configuration

> **Note:** `tasks.json` is generated automatically by the application at runtime to store task data. It is not included as a source-file deliverable.
## Development Outcome

The project demonstrates practical implementation of:

- Python programming
- Object-oriented programming
- Modular software design
- File handling
- JSON serialization
- Input validation
- Exception handling
- Automated testing
- Git and GitHub workflow

The application provides a functional command-line solution for managing tasks while maintaining task data between application sessions.
## Current Limitations

Although the application provides the required task management features, it currently has some limitations:

- The application is command-line based.
- There is no graphical user interface.
- Tasks are stored locally in a JSON file.
- There is no user authentication.
- Tasks do not currently have priorities or deadlines.
- The application is designed for local, single-user usage.

## Future Improvements

The following features could be added in future versions:

- Task priorities such as High, Medium, and Low
- Due dates and reminders
- Task search functionality
- Task categories
- Editing existing tasks
- Graphical user interface
- Database-based storage
- User authentication
- Export tasks to CSV
- Cloud-based task synchronization

## Conclusion

The To-Do List Manager successfully implements the core requirements of a command-line task management application.

The project demonstrates practical knowledge of Python programming, object-oriented programming, modular software design, JSON file handling, input validation, exception handling, and automated testing.

The application provides four main task operations: adding tasks, viewing tasks, marking tasks as completed, and removing tasks. Task information is also persisted using a JSON file, allowing data to remain available between application sessions.

The project was tested using Python's built-in `unittest` framework. A total of 7 automated test cases were executed successfully, with all 7 tests passing.

The modular structure of the project makes it easier to maintain and provides a foundation for future improvements such as database storage, task priorities, deadlines, authentication, and a graphical user interface.