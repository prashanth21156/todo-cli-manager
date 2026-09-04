import unittest
from todo import Task


class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task("Learn Python")

        self.assertEqual(task.title, "Learn Python")
        self.assertFalse(task.completed)

    def test_mark_completed(self):
        task = Task("Learn Python")

        task.mark_completed()

        self.assertTrue(task.completed)


class TestTaskList(unittest.TestCase):

    def test_add_task(self):
        tasks = []

        task = Task("Learn Python")
        tasks.append(task)

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Learn Python")

    def test_remove_task(self):
        tasks = []

        task1 = Task("Learn Python")
        task2 = Task("Practice Git")

        tasks.append(task1)
        tasks.append(task2)

        removed_task = tasks.pop(0)

        self.assertEqual(removed_task.title, "Learn Python")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Practice Git")


if __name__ == "__main__":
    unittest.main()