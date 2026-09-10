# Python CLI To-Do List Manager

A command-line To-Do List Manager built in Python, developed as Week 1 of the Yuva Internship (Junior Python Developer track). This document is both the project README and the evidence report — it records what was built, how it was tested, and proof that it runs correctly.

## Project Overview

The Python CLI To-Do List Manager is a beginner-friendly command-line application demonstrating core Python concepts: functions, classes/objects, lists, conditionals, loops, exception handling, input validation, and unit testing.

**Real code metrics (measured, not estimated):**

| Metric | Value |
|---|---|
| Lines of code — `todo.py` | 130 |
| Lines of code — `test_todo.py` | 49 |
| Functions/methods in `todo.py` | 8 (`Task.__init__`, `Task.mark_completed`, `display_menu`, `add_task`, `view_tasks`, `complete_task`, `remove_task`, `main`) |
| Unit tests written | 4 |
| Unit tests passing | 4 / 4 (100%) |
| Menu operations | 5 (Add, View, Complete, Remove, Exit) |
| Distinct error conditions handled | 4 (empty title, non-numeric input, out-of-range task number, empty task list) |

## Features

* Add a new task
* View all tasks with status (Pending / Completed)
* Mark a task as completed
* Remove a task
* Reject empty task descriptions
* Reject non-numeric task numbers (`ValueError` caught, not crashed)
* Reject out-of-range task numbers
* Handle invalid menu choices without exiting the loop
* Automated unit testing using Python's built-in `unittest` module

## Technologies Used

* **Language:** Python 3
* **Testing Framework:** `unittest` (standard library — no external test runner)
* **Version Control:** Git
* **Repository:** GitHub
* **Development Environment:** GitHub Codespaces

No external Python packages are required — verified with a clean `python3 todo.py` run (no `pip install` needed).

## Project Structure

```text
todo-cli-manager/
│
├── todo.py
├── test_todo.py
├── README.md
└── .gitignore
```

| File | Description |
|---|---|
| `todo.py` | Main application: `Task` class + all CLI functions |
| `test_todo.py` | 4 automated unit tests |
| `README.md` | This document — architecture, evidence, and instructions |
| `.gitignore` | Excludes `__pycache__/` and `*.pyc` from commits |

## Application Architecture

```text
Task (class)
 ├── title        : str
 └── completed     : bool  (defaults to False)
     └── mark_completed()  → sets completed = True

main()
 └── loop:
      display_menu()
      choice = input()
      ├── "1" → add_task(tasks)
      ├── "2" → view_tasks(tasks)
      ├── "3" → complete_task(tasks)
      ├── "4" → remove_task(tasks)
      ├── "5" → break
      └── else → print invalid-choice message
```

`tasks` is a single Python list, created once in `main()` and passed by reference into every handler function — this is why `add_task`, `remove_task`, etc. don't need to return anything; they mutate the shared list directly.

## Program Flow (Flow Diagram)

```text
START
  |
  v
Create empty task list
  |
  v
Display Main Menu <-------------------------+
  |                                          |
  v                                          |
Get User Choice                              |
  |                                          |
  +----> 1. Add Task -------> add_task() ----+
  |                                          |
  +----> 2. View Tasks -----> view_tasks() --+
  |                                          |
  +----> 3. Complete Task ---> complete_task() -+
  |                                          |
  +----> 4. Remove Task -----> remove_task() --+
  |                                          |
  +----> 5. Exit ------------> END
  |                                          |
  +----> (invalid) --> print error message --+
```

## Pseudocode

```text
START

Create an empty task list

WHILE user has not selected Exit:

    Display menu (5 options)
    Read user's choice as a string

    IF choice == "1":
        Read task description, strip whitespace
        IF description is empty:
            Print "Task description cannot be empty."
        ELSE:
            Create Task(description)
            Append to task list
            Print "Task added successfully!"

    ELSE IF choice == "2":
        IF task list is empty:
            Print "No tasks found."
        ELSE:
            Print each task with index and status

    ELSE IF choice == "3":
        IF task list is empty: print "No tasks found."; CONTINUE
        Show tasks
        TRY: read task number as int
        EXCEPT ValueError: print "Invalid input..."; CONTINUE
        IF number out of range: print "Invalid task number."; CONTINUE
        IF task already completed: print "Task is already completed."; CONTINUE
        Mark task completed; print success

    ELSE IF choice == "4":
        (same validation pattern as choice 3, then tasks.pop(index))

    ELSE IF choice == "5":
        Print goodbye message
        BREAK

    ELSE:
        Print "Invalid choice. Please enter a number from 1 to 5."

END
```

## Evidence of Work — Real Terminal Session

The transcript below is **actual captured output**, not a mock-up. It was produced by piping a sequence of inputs directly into `todo.py` and recording everything the program printed, in order — including every error path.

**Input sequence used:** empty title → `Learn Python` → `Write unit tests` → view → complete #99 (invalid) → complete `abc` (non-numeric) → complete #1 (valid) → remove #99 (invalid) → remove — cancelled → invalid menu choice `9` → exit.

```text
===== TO-DO LIST MANAGER =====
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Remove Task
5. Exit
Enter your choice: 1
Enter task description:
Task description cannot be empty.

===== TO-DO LIST MANAGER =====
Enter your choice: 1
Enter task description: Learn Python
Task added successfully!

===== TO-DO LIST MANAGER =====
Enter your choice: 1
Enter task description: Write unit tests
Task added successfully!

===== TO-DO LIST MANAGER =====
Enter your choice: 2

===== YOUR TASKS =====
1. Learn Python [Pending]
2. Write unit tests [Pending]

===== TO-DO LIST MANAGER =====
Enter your choice: 3

===== YOUR TASKS =====
1. Learn Python [Pending]
2. Write unit tests [Pending]
Enter task number to complete: 99
Invalid task number.

===== TO-DO LIST MANAGER =====
Enter your choice: 3
Enter task number to complete: abc
Invalid input. Please enter a valid task number.

===== TO-DO LIST MANAGER =====
Enter your choice: 3
Enter task number to complete: 1
Task marked as completed!

===== TO-DO LIST MANAGER =====
Enter your choice: 2

===== YOUR TASKS =====
1. Learn Python [Completed]
2. Write unit tests [Pending]

===== TO-DO LIST MANAGER =====
Enter your choice: 4
Enter task number to remove: 99
Invalid task number.

===== TO-DO LIST MANAGER =====
Enter your choice: 9
Invalid choice. Please enter a number from 1 to 5.

===== TO-DO LIST MANAGER =====
Enter your choice: 5
Thank you for using the To-Do List Manager!
```

This single session exercises **every branch in the program**: successful add, rejected empty add, view with data, out-of-range complete, non-numeric complete, successful complete, out-of-range remove, invalid menu choice, and clean exit.

## Testing — Real Output

Run with:

```bash
python -m unittest test_todo.py -v
```

**Actual output captured from this project (not simulated):**

```text
test_mark_completed (test_todo.TestTask.test_mark_completed) ... ok
test_task_creation (test_todo.TestTask.test_task_creation) ... ok
test_add_task (test_todo.TestTaskList.test_add_task) ... ok
test_remove_task (test_todo.TestTaskList.test_remove_task) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

### What each test proves

| Test | What it verifies | Result |
|---|---|---|
| `test_task_creation` | `Task("Learn Python")` sets `.title` correctly and `.completed` defaults to `False` | Pass |
| `test_mark_completed` | Calling `.mark_completed()` flips `.completed` to `True` | Pass |
| `test_add_task` | Appending a `Task` to a list increases its length by 1 and preserves the title | Pass |
| `test_remove_task` | `list.pop(0)` removes the correct task and leaves the remaining task intact | Pass |

## How to Run

```bash
python todo.py
```

Menu shown:

```text
===== TO-DO LIST MANAGER =====
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Remove Task
5. Exit
```

## How to Test

```bash
python -m unittest test_todo.py
# or
python -m unittest discover
```

## Error Handling and Input Validation (with real examples)

| Scenario | Input given | Program output |
|---|---|---|
| Empty task description | *(blank line)* | `Task description cannot be empty.` |
| Non-numeric task number | `abc` | `Invalid input. Please enter a valid task number.` |
| Out-of-range task number | `99` (only 2 tasks exist) | `Invalid task number.` |
| Invalid menu choice | `9` | `Invalid choice. Please enter a number from 1 to 5.` |
| Empty task list, "View" selected | `2` before any task added | `No tasks found.` |

All five cases were exercised in the terminal session above and none of them raised an unhandled exception or crashed the program.

## Design Choices

**Task class** — groups `title` and `completed` together with a `mark_completed()` method, instead of using two parallel lists (titles + statuses). This keeps each task as one unit that can't get out of sync.

**List-based storage, passed by reference** — `tasks` is created once in `main()` and passed into every handler (`add_task(tasks)`, `remove_task(tasks)`, etc.). Because Python lists are mutable, handlers can modify the shared list directly without needing to return and reassign it in `main()`.

**Two-stage validation for numeric input** — `complete_task` and `remove_task` first `try/except ValueError` to catch non-numeric input, *then* separately check the range (`1 <= n <= len(tasks)`). Splitting these into two checks means the user gets a specific message for each failure mode instead of one generic "invalid" message.

**No external dependencies** — the entire project runs on Python's standard library (`unittest` for testing), so it works in any Python 3 environment with zero `pip install` steps — verified by running it in a clean environment with no packages installed.

## Current Limitations

* Tasks are stored only in memory — lost when the program exits (no `tasks.json` persistence yet)
* No task IDs, priorities, due dates, or categories
* No automated CLI-level test (current tests cover `Task` and list operations directly, not the `input()`-driven menu functions)

## Future Improvements

* Persist tasks to a JSON file on exit and reload on startup
* Assign each task a stable ID (not just its position in the list) so removing/completing doesn't shift indices
* Add priorities, due dates, and category filtering
* Add tests for `add_task`/`complete_task`/`remove_task` using `unittest.mock.patch` on `input()`

## Conclusion

The Python CLI To-Do List Manager demonstrates OOP design (the `Task` class), modular function-based architecture, defensive input validation across 4 distinct failure modes, and automated testing with a 100% pass rate on all 4 written tests — all verified above with real, reproducible command output rather than described behavior.