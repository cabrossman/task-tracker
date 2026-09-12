import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import tasks


class TaskTests(unittest.TestCase):
    def setUp(self):
        patcher = patch.object(tasks, "tasks", [])
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_add_task_starts_incomplete(self):
        tasks.add_task("Buy groceries")

        self.assertEqual(tasks.tasks, [
            {"name": "Buy groceries", "completed": False}
        ])

    def test_add_tasks_preserves_order(self):
        tasks.add_task("Buy groceries")
        tasks.add_task("Study ML")

        self.assertEqual(
            [task["name"] for task in tasks.tasks],
            ["Buy groceries", "Study ML"],
        )

    def test_complete_task_only_changes_matching_task(self):
        tasks.add_task("Buy groceries")
        tasks.add_task("Study ML")

        tasks.complete_task("Study ML")

        self.assertEqual(tasks.tasks, [
            {"name": "Buy groceries", "completed": False},
            {"name": "Study ML", "completed": True},
        ])

    def test_complete_unknown_task_leaves_tasks_unchanged(self):
        tasks.add_task("Buy groceries")

        tasks.complete_task("Unknown task")

        self.assertEqual(tasks.tasks, [
            {"name": "Buy groceries", "completed": False}
        ])

    def test_completing_task_twice_keeps_it_completed(self):
        tasks.add_task("Study ML")

        tasks.complete_task("Study ML")
        tasks.complete_task("Study ML")

        self.assertEqual(tasks.tasks, [
            {"name": "Study ML", "completed": True}
        ])

    def test_complete_task_with_empty_list(self):
        tasks.complete_task("Unknown task")

        self.assertEqual(tasks.tasks, [])

    def test_show_tasks_displays_status_and_name(self):
        tasks.add_task("Buy groceries")
        tasks.add_task("Study ML")
        tasks.complete_task("Study ML")
        output = io.StringIO()

        with redirect_stdout(output):
            tasks.show_tasks()

        self.assertEqual(output.getvalue(), "[ ] Buy groceries\n[✓] Study ML\n")

    def test_show_tasks_with_empty_list_prints_nothing(self):
        output = io.StringIO()

        with redirect_stdout(output):
            tasks.show_tasks()

        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
