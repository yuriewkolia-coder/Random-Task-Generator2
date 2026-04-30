from abc import ABC, abstractmethod
import random
from .task import Task, TaskType, Difficulty


class TaskCreator(ABC):
    """Абстрактный класс создателя задач"""

    @abstractmethod
    def create_task(self, description: str = None) -> Task:
        pass


class WorkTaskCreator(TaskCreator):
    """Создатель рабочих задач"""

    def create_task(self, description: str = None) -> Task:
        descriptions = [
            "Написать отчет за неделю",
            "Провести встречу с командой",
            "Завершить проект до дедлайна",
            "Оптимизировать рабочий процесс",
            "Изучить новый инструмент для работы"
        ]
        desc = description or random.choice(descriptions)
        return Task(desc, TaskType.WORK, Difficulty.MEDIUM)


class SportTaskCreator(TaskCreator):
    """Создатель спортивных задач"""

    def create_task(self, description: str = None) -> Task:
        descriptions = [
            "Пробежать 5 км",
            "Сделать 100 приседаний",
            "Пойти в тренажерный зал",
            "Позаниматься йогой 30 минут",
            "Сыграть в футбол с друзьями"
        ]
        desc = description or random.choice(descriptions)
        difficulty = random.choice([Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD])
        return Task(desc, TaskType.SPORT, difficulty)


class StudyTaskCreator(TaskCreator):
    """Создатель учебных задач"""

    def create_task(self, description: str = None) -> Task:
        descriptions = [
            "Прочитать главу книги по программированию",
            "Решить 10 задач на алгоритмы",
            "Посмотреть лекцию по математике",
            "Выучить 20 новых слов на английском",
            "Написать тестовое задание"
        ]
        desc = description or random.choice(descriptions)
        return Task(desc, TaskType.STUDY, Difficulty.HARD)


class HomeTaskCreator(TaskCreator):
    """Создатель домашних задач"""

    def create_task(self, description: str = None) -> Task:
        descriptions = [
            "Убраться в комнате",
            "Приготовить ужин",
            "Починить сломанную вещь",
            "Полить цветы",
            "Сходить в магазин за продуктами"
        ]
        desc = description or random.choice(descriptions)
        return Task(desc, TaskType.HOME, Difficulty.EASY)


class HealthTaskCreator(TaskCreator):
    """Создатель задач о здоровье"""

    def create_task(self, description: str = None) -> Task:
        descriptions = [
            "Сходить к врачу на осмотр",
            "Выспаться 8 часов",
            "Пить воду в течение дня (2 литра)",
            "Сделать зарядку утром",
            "Практиковать медитацию 15 минут"
        ]
        desc = description or random.choice(descriptions)
        difficulty = random.choice([Difficulty.EASY, Difficulty.MEDIUM])
        return Task(desc, TaskType.HEALTH, difficulty)


class TaskFactory:
    """Фабрика для создания задач разных типов"""

    def __init__(self):
        self.creators = {
            TaskType.WORK: WorkTaskCreator(),
            TaskType.SPORT: SportTaskCreator(),
            TaskType.STUDY: StudyTaskCreator(),
            TaskType.HOME: HomeTaskCreator(),
            TaskType.HEALTH: HealthTaskCreator()
        }

    def generate_random_task(self) -> Task:
        """Генерирует случайную задачу случайного типа"""
        task_type = random.choice(list(TaskType))
        return self.creators[task_type].create_task()

    def create_task_by_type(self, task_type: TaskType, description: str = None) -> Task:
        """Создает задачу конкретного типа"""
        if task_type not in self.creators:
            raise ValueError(f"Неизвестный тип задачи: {task_type}")
        return self.creators[task_type].create_task(description)