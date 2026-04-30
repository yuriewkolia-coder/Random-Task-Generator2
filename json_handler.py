import json
import os
from typing import List
from models.task import Task


class JSONHandler:
    """Обработчик JSON файлов"""

    def __init__(self, filename: str = "tasks_history.json"):
        self.filename = filename

    def save_tasks(self, tasks: List[Task]) -> bool:
        """Сохраняет задачи в JSON файл"""
        try:
            tasks_data = [task.to_dict() for task in tasks]
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(tasks_data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            return False

    def load_tasks(self) -> List[Task]:
        """Загружает задачи из JSON файла"""
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                tasks_data = json.load(f)

            tasks = []
            for task_data in tasks_data:
                try:
                    task = Task.from_dict(task_data)
                    tasks.append(task)
                except (KeyError, ValueError) as e:
                    print(f"Ошибка при загрузке задачи: {e}")
                    continue
            return tasks
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")
            return []