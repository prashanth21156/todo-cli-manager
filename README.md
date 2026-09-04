# Python CLI To-Do List Manager

## Project Overview

A simple command-line To-Do List Manager built using Python. The application allows users to add, view, complete, and remove tasks through an interactive CLI menu.

## Features

* Add a new task
* View all tasks
* Mark a task as completed
* Remove a task
* Validate user input
* Handle invalid menu choices gracefully

## Application Architecture

The application will use a modular design with functions responsible for individual operations.

### Main Components

1. **Main Menu**

   * Displays available options.
   * Gets the user's choice.
   * Calls the appropriate function.

2. **Add Task**

   * Accepts a task description.
   * Validates the input.
   * Adds the task to the task list.

3. **View Tasks**

   * Displays all available tasks.
   * Shows whether each task is pending or completed.

4. **Complete Task**

   * Allows the user to select a task.
   * Changes its status to completed.

5. **Remove Task**

   * Allows the user to select a task.
   * Removes it from the task list.

6. **Input Validation**

   * Handles invalid menu choices.
   * Handles invalid task numbers.
   * Prevents empty task descriptions.

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
  +----> 1. Add Task --------> Add Task ------+
  |                                           |
  +----> 2. View Tasks -------> View Tasks ---+
  |                                           |
  +----> 3. Complete Task ----> Complete -----+
  |                                           |
  +----> 4. Remove Task ------> Remove -------+
  |                                           |
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
        Validate task description
        Add task to task list

    ELSE IF choice is View Tasks:
        Display all tasks

    ELSE IF choice is Complete Task:
        Display tasks
        Get task number
        Validate task number
        Mark selected task as completed

    ELSE IF choice is Remove Task:
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

## Development Approach

The application will be developed incrementally. Each feature will be implemented and tested separately before moving to the next feature.
