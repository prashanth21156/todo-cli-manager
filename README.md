# Python CLI To-Do List Manager

A simple and user-friendly command-line To-Do List Manager built using Python. The application allows users to manage their daily tasks through an interactive terminal-based menu.

## Project Overview

The Python CLI To-Do List Manager is a beginner-friendly command-line application designed to demonstrate core Python programming concepts such as:

* Functions
* Classes and objects
* Lists
* Conditional statements
* Loops
* Exception handling
* Input validation
* Unit testing

The application allows users to add, view, complete, and remove tasks.

## Features

* Add a new task
* View all tasks
* Mark a task as completed
* Remove a task
* Validate user input
* Handle invalid menu choices
* Handle invalid task numbers
* Prevent empty task descriptions
* Display clear success and error messages
* Automated unit testing using Python's built-in `unittest` module

## Technologies Used

* **Programming Language:** Python 3
* **Testing Framework:** unittest
* **Version Control:** Git
* **Repository:** GitHub
* **Development Environment:** GitHub Codespaces

No external Python packages are required.

## Project Structure

```text
todo-cli-manager/
│
├── todo.py
├── test_todo.py
├── README.md
└── .gitignore
```

### File Description

| File           | Description                                                                  |
| -------------- | ---------------------------------------------------------------------------- |
| `todo.py`      | Main application containing the To-Do List functionality                     |
| `test_todo.py` | Automated unit tests                                                         |
| `README.md`    | Project documentation                                                        |
| `.gitignore`   | Prevents unnecessary Python files such as `__pycache__` from being committed |

## Application Architecture

The application follows a simple modular structure where different functions are responsible for different operations.

### Main Components

1. **Main Menu**

   * Displays available options.
   * Gets the user's choice.
   * Calls the appropriate function.

2. **Task Class**

   * Represents an individual task.
   * Stores the task title.
   * Stores the completion status.
   * Provides a method to mark the task as completed.

3. **Add Task**

   * Accepts a task description.
   * Validates the input.
   * Creates a new task.
   * Adds the task to the task list.

4. **View Tasks**

   * Displays all tasks.
   * Shows the task number.
   * Shows whether each task is Pending or Completed.

5. **Complete Task**

   * Displays the available tasks.
   * Allows the user to select a task.
   * Changes the selected task status to Completed.

6. **Remove Task**

   * Displays the available tasks.
   * Allows the user to select a task.
   * Removes the selected task from the list.

7. **Input Validation**

   * Prevents empty task descriptions.
   * Handles non-numeric task numbers.
   * Handles invalid task numbers.
   * Handles invalid menu choices.

## Program Flow

```text
START
  |
  v
Display Main Menu
  |
  v
Get User Choice
  |
  +----> 1. Add Task -------> Add Task ------+
  |                                          |
  +----> 2. View Tasks ------> View Tasks ---+
  |                                          |
  +----> 3. Complete Task ---> Complete -----+
  |                                          |
  +----> 4. Remove Task -----> Remove -------+
  |                                          |
  +----> 5. Exit ------------> END
  |
  v
Handle Invalid Choice
  |
  v
Display Main Menu Again
```

## Pseudocode

```text
START

Create an empty task list

WHILE user has not selected Exit:

    Display menu

    Get user's choice

    IF choice is Add Task:
        Get task description
        Remove unnecessary spaces
        Validate task description
        Create a task
        Add task to task list

    ELSE IF choice is View Tasks:
        Check whether task list is empty
        Display all tasks and their status

    ELSE IF choice is Complete Task:
        Check whether tasks exist
        Display tasks
        Get task number
        Validate task number
        Mark selected task as completed

    ELSE IF choice is Remove Task:
        Check whether tasks exist
        Display tasks
        Get task number
        Validate task number
        Remove selected task

    ELSE IF choice is Exit:
        Display exit message
        END PROGRAM

    ELSE:
        Display invalid choice message

END
```

## How to Run

### 1. Clone the Repository

Clone the project from GitHub and open the project folder.

### 2. Run the Application

Open a terminal in the project directory and run:

```bash
python todo.py
```

The main menu will appear:

```text
===== TO-DO LIST MANAGER =====
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Remove Task
5. Exit
```

### 3. Follow the Menu

Enter a number from `1` to `5` to perform an operation.

## Example Usage

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

Viewing the task:

```text
===== YOUR TASKS =====
1. Learn Python [Pending]
```

Completing the task:

```text
Enter task number to complete: 1
Task marked as completed!
```

The task will then appear as:

```text
1. Learn Python [Completed]
```

## Error Handling and Input Validation

The application is designed to handle common user input errors without crashing.

### Empty Task

```text
Enter task description:
Task description cannot be empty.
```

### Invalid Menu Choice

```text
Enter your choice: 99
Invalid choice. Please enter a number from 1 to 5.
```

### Invalid Task Number

```text
Enter task number to remove: 99
Invalid task number.
```

### Non-Numeric Task Number

```text
Enter task number to remove: abc
Invalid input. Please enter a valid task number.
```

### Empty Task List

```text
No tasks found.
```

## Testing

The project uses Python's built-in `unittest` framework.

### Run the Tests

Run:

```bash
python -m unittest test_todo.py
```

You can also automatically discover test files using:

```bash
python -m unittest discover
```

### Test Cases

The automated tests verify:

1. Task creation
2. Initial task status
3. Marking a task as completed
4. Adding a task to the task list
5. Removing a task from the task list

Example successful test output:

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## Design Choices

### Task Class

A `Task` class is used to represent each individual task. This makes the application easier to maintain and allows task-related properties and operations to be grouped together.

### List-Based Storage

Tasks are currently stored in a Python list. This keeps the application simple and is suitable for a basic CLI application.

### Modular Functions

Each major operation is implemented as a separate function. This improves readability, maintainability, and testing.

### Input Validation

User input is validated before performing operations. This prevents common errors and makes the application more user-friendly.

### No External Dependencies

The project uses only Python's standard library, making it easy to run without installing additional packages.

## Development Approach

The application was developed incrementally. Each feature was implemented, tested, and verified before moving to the next feature.

Development stages included:

1. Project setup
2. Application architecture
3. CLI menu
4. Task data structure
5. Add task functionality
6. View task functionality
7. Complete task functionality
8. Remove task functionality
9. Error handling and input validation
10. Automated testing
11. Documentation

## Current Limitations

* Tasks are stored only in memory.
* Tasks are lost when the application is closed.
* No database or file-based storage is currently implemented.
* There is no user authentication.

## Future Improvements

Possible future enhancements include:

* Save tasks to a JSON or CSV file
* Load saved tasks when the application starts
* Add task priorities
* Add due dates
* Add task categories
* Search and filter tasks
* Add a database for persistent storage
* Create a graphical or web-based interface

## Conclusion

The Python CLI To-Do List Manager demonstrates fundamental Python programming, modular application design, input validation, error handling, and automated testing.

The project provides a strong foundation for developing more advanced task-management applications in the future.
