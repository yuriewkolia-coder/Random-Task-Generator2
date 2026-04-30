from collections import deque
from typing import List, Optional
from models.task import Task, TaskType, Difficulty
from models.task_factory import TaskFactory


class TaskManager:
    """Управляет генерацией и хранением задач"""

    def __init__(self, max_history: int = 100):
        self.factory = TaskFactory()
        self.history = deque(maxlen=max_history)

    def generate_task(self) -> Task:
        """Генерирует случайную задачу и добавляет в историю"""
        task = self.factory.generate_random_task()
        self.history.append(task)
        return task

    def add_custom_task(self, description: str, task_type: TaskType, difficulty: Difficulty) -> Task:
        """Добавляет пользовательскую задачу"""
        if not description or len(description.strip()) == 0:
            raise ValueError("Описание задачи не может быть пустым")

        if len(description) > 200:
            raise ValueError("Описание задачи не должно превышать 200 символов")

        task = Task(description.strip(), task_type, difficulty)
        self.history.append(task)
        return task

    def filter_tasks_by_type(self, task_type: TaskType) -> List[Task]:
        """Фильтрует задачи по типу"""
        return [task for task in self.history if task.type == task_type]

    def filter_tasks_by_difficulty(self, difficulty: Difficulty) -> List[Task]:
        """Фильтрует задачи по сложности"""
        return [task for task in self.history if task.difficulty == difficulty]

    def get_all_tasks(self) -> List[Task]:
        """Возвращает все задачи из истории"""
        return list(self.history)

    def clear_history(self):
        """Очищает историю"""
        self.history.clear()

    def get_history_size(self) -> int:
        """Возвращает размер истории"""
        return len(self.history)