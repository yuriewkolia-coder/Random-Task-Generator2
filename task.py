from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class TaskType(Enum):
    WORK = "Работа"
    SPORT = "Спорт"
    STUDY = "Учеба"
    HOME = "Дом"
    HEALTH = "Здоровье"


class Difficulty(Enum):
    EASY = "Легкая"
    MEDIUM = "Средняя"
    HARD = "Сложная"


@dataclass
class Task:
    """Базовый класс задачи"""
    description: str
    type: TaskType
    difficulty: Difficulty
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Преобразует задачу в словарь для JSON"""
        return {
            'description': self.description,
            'type': self.type.value,
            'difficulty': self.difficulty.value,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        """Создает задачу из словаря"""
        task_type = TaskType(data['type'])
        difficulty = Difficulty(data['difficulty'])
        task = cls(data['description'], task_type, difficulty)
        task.created_at = data['created_at']
        return task

    def __str__(self):
        return f"[{self.type.value}] {self.description} (Сложность: {self.difficulty.value}) - {self.created_at}"