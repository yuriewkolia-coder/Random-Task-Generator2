import unittest
from models.task import Task, TaskType, Difficulty
from services.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_generate_task(self):
        """Позитивный тест: генерация задачи"""
        task = self.manager.generate_task()
        self.assertIsNotNone(task)
        self.assertIsInstance(task, Task)
        self.assertEqual(len(self.manager.history), 1)

    def test_add_custom_task_positive(self):
        """Позитивный тест: добавление пользовательской задачи"""
        task = self.manager.add_custom_task("Тестовая задача", TaskType.WORK, Difficulty.EASY)
        self.assertIsNotNone(task)
        self.assertEqual(task.description, "Тестовая задача")
        self.assertEqual(task.type, TaskType.WORK)

    def test_add_custom_task_empty_description(self):
        """Негативный тест: пустое описание"""
        with self.assertRaises(ValueError):
            self.manager.add_custom_task("", TaskType.WORK, Difficulty.EASY)

    def test_add_custom_task_whitespace_description(self):
        """Негативный тест: описание из пробелов"""
        with self.assertRaises(ValueError):
            self.manager.add_custom_task("   ", TaskType.WORK, Difficulty.EASY)

    def test_add_custom_task_long_description(self):
        """Негативный тест: слишком длинное описание"""
        long_description = "a" * 201
        with self.assertRaises(ValueError):
            self.manager.add_custom_task(long_description, TaskType.WORK, Difficulty.EASY)

    def test_filter_by_type(self):
        """Позитивный тест: фильтрация по типу"""
        self.manager.add_custom_task("Рабочая задача", TaskType.WORK, Difficulty.EASY)
        self.manager.add_custom_task("Спортивная задача", TaskType.SPORT, Difficulty.MEDIUM)

        filtered = self.manager.filter_tasks_by_type(TaskType.WORK)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].type, TaskType.WORK)

    def test_filter_by_difficulty(self):
        """Позитивный тест: фильтрация по сложности"""
        self.manager.add_custom_task("Легкая задача", TaskType.WORK, Difficulty.EASY)
        self.manager.add_custom_task("Средняя задача", TaskType.SPORT, Difficulty.MEDIUM)

        filtered = self.manager.filter_tasks_by_difficulty(Difficulty.EASY)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].difficulty, Difficulty.EASY)

    def test_clear_history(self):
        """Позитивный тест: очистка истории"""
        self.manager.generate_task()
        self.assertEqual(len(self.manager.history), 1)
        self.manager.clear_history()
        self.assertEqual(len(self.manager.history), 0)


if __name__ == '__main__':
    unittest.main()