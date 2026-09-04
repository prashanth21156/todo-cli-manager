import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from models import Task
from todo_manager import load_tasks, save_tasks


class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task(1, "Learn Python")

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Learn Python")
        self.assertFalse(task.completed)

    def test_mark_completed(self):
        task = Task(1, "Learn Python")

        task.mark_completed()

        self.assertTrue(task.completed)


class TestTaskList(unittest.TestCase):

    def test_add_task(self):
        tasks = []

        task = Task(1, "Learn Python")
        tasks.append(task)

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Learn Python")

    def test_remove_task(self):
        tasks = []

        task1 = Task(1, "Learn Python")
        task2 = Task(2, "Practice Git")

        tasks.append(task1)
        tasks.append(task2)

        removed_task = tasks.pop(0)

        self.assertEqual(removed_task.title, "Learn Python")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Practice Git")


class TestTaskPersistence(unittest.TestCase):

    def test_task_to_dict(self):
        task = Task(3, "Read docs", True)

        self.assertEqual(
            task.to_dict(),
            {"id": 3, "title": "Read docs", "completed": True},
        )

    def test_save_and_load_tasks(self):
        tasks = [Task(1, "Learn Python"), Task(2, "Practice Git", True)]

        with TemporaryDirectory() as directory:
            file_path = Path(directory) / "tasks.json"
            save_tasks(tasks, file_path)
            loaded_tasks = load_tasks(file_path)

        self.assertEqual([task.to_dict() for task in loaded_tasks], [
            {"id": 1, "title": "Learn Python", "completed": False},
            {"id": 2, "title": "Practice Git", "completed": True},
        ])

    def test_load_missing_file_returns_empty_list(self):
        with TemporaryDirectory() as directory:
            file_path = Path(directory) / "missing.json"

            self.assertEqual(load_tasks(file_path), [])


if __name__ == "__main__":
    unittest.main()