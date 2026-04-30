import sys
from models.task import TaskType, Difficulty
from services.task_manager import TaskManager
from services.json_handler import JSONHandler


class RandomTaskGenerator:
    """Главное консольное приложение"""

    def __init__(self):
        self.task_manager = TaskManager()
        self.json_handler = JSONHandler()
        self.load_saved_tasks()

    def load_saved_tasks(self):
        """Загружает сохраненные задачи"""
        saved_tasks = self.json_handler.load_tasks()
        for task in saved_tasks:
            self.task_manager.history.append(task)
        print(f"Загружено {len(saved_tasks)} задач из истории")

    def save_current_history(self):
        """Сохраняет текущую историю"""
        tasks = self.task_manager.get_all_tasks()
        if self.json_handler.save_tasks(tasks):
            print("✓ История успешно сохранена")
        else:
            print("✗ Ошибка при сохранении истории")

    def display_menu(self):
        """Отображает главное меню"""
        print("\n" + "=" * 50)
        print("ГЕНЕРАТОР СЛУЧАЙНЫХ ЗАДАЧ")
        print("=" * 50)
        print("1. Сгенерировать случайную задачу")
        print("2. Добавить свою задачу")
        print("3. Показать историю задач")
        print("4. Фильтровать задачи по типу")
        print("5. Фильтровать задачи по сложности")
        print("6. Сохранить историю")
        print("7. Очистить историю")
        print("0. Выход")
        print("=" * 50)

    def generate_random_task(self):
        """Генерирует случайную задачу"""
        task = self.task_manager.generate_task()
        print("\n✨ Сгенерирована новая задача:")
        print(f"   {task}")

    def add_custom_task(self):
        """Добавляет пользовательскую задачу"""
        print("\n📝 Добавление новой задачи:")

        # Ввод описания
        description = input("Введите описание задачи: ").strip()
        if not description:
            print("✗ Ошибка: описание не может быть пустым")
            return

        # Выбор типа
        print("\nТипы задач:")
        for i, task_type in enumerate(TaskType, 1):
            print(f"{i}. {task_type.value}")

        try:
            type_choice = int(input("Выберите тип (1-5): "))
            if type_choice < 1 or type_choice > len(TaskType):
                raise ValueError
            task_type = list(TaskType)[type_choice - 1]
        except (ValueError, IndexError):
            print("✗ Ошибка: неверный выбор типа")
            return

        # Выбор сложности
        print("\nУровни сложности:")
        for i, difficulty in enumerate(Difficulty, 1):
            print(f"{i}. {difficulty.value}")

        try:
            diff_choice = int(input("Выберите сложность (1-3): "))
            if diff_choice < 1 or diff_choice > len(Difficulty):
                raise ValueError
            difficulty = list(Difficulty)[diff_choice - 1]
        except (ValueError, IndexError):
            print("✗ Ошибка: неверный выбор сложности")
            return

        try:
            task = self.task_manager.add_custom_task(description, task_type, difficulty)
            print(f"\n✓ Задача добавлена:")
            print(f"   {task}")
        except ValueError as e:
            print(f"✗ Ошибка: {e}")

    def show_history(self):
        """Показывает историю задач"""
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("\n📭 История пуста. Сгенерируйте или добавьте задачи.")
            return

        print(f"\n📋 История задач (всего: {len(tasks)}):")
        print("-" * 50)
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("-" * 50)

    def filter_by_type(self):
        """Фильтрует задачи по типу"""
        print("\n🔍 Фильтр по типу задачи:")
        for i, task_type in enumerate(TaskType, 1):
            print(f"{i}. {task_type.value}")

        try:
            type_choice = int(input("Выберите тип (1-5): "))
            if type_choice < 1 or type_choice > len(TaskType):
                raise ValueError
            task_type = list(TaskType)[type_choice - 1]

            filtered = self.task_manager.filter_tasks_by_type(task_type)
            if not filtered:
                print(f"\n📭 Нет задач типа '{task_type.value}'")
                return

            print(f"\n📋 Задачи типа '{task_type.value}':")
            print("-" * 50)
            for task in filtered:
                print(f"   {task}")
            print("-" * 50)
        except (ValueError, IndexError):
            print("✗ Ошибка: неверный выбор")

    def filter_by_difficulty(self):
        """Фильтрует задачи по сложности"""
        print("\n🔍 Фильтр по сложности:")
        for i, difficulty in enumerate(Difficulty, 1):
            print(f"{i}. {difficulty.value}")

        try:
            diff_choice = int(input("Выберите сложность (1-3): "))
            if diff_choice < 1 or diff_choice > len(Difficulty):
                raise ValueError
            difficulty = list(Difficulty)[diff_choice - 1]

            filtered = self.task_manager.filter_tasks_by_difficulty(difficulty)
            if not filtered:
                print(f"\n📭 Нет задач сложности '{difficulty.value}'")
                return

            print(f"\n📋 Задачи сложности '{difficulty.value}':")
            print("-" * 50)
            for task in filtered:
                print(f"   {task}")
            print("-" * 50)
        except (ValueError, IndexError):
            print("✗ Ошибка: неверный выбор")

    def clear_history(self):
        """Очищает историю с подтверждением"""
        confirm = input("\n⚠️ Вы уверены, что хотите очистить всю историю? (y/n): ")
        if confirm.lower() == 'y':
            self.task_manager.clear_history()
            print("✓ История очищена")
        else:
            print("Операция отменена")

    def run(self):
        """Запускает основный цикл приложения"""
        print("\nДобро пожаловать в Генератор случайных задач!")

        while True:
            self.display_menu()
            choice = input("\nВыберите действие: ")

            if choice == '1':
                self.generate_random_task()
            elif choice == '2':
                self.add_custom_task()
            elif choice == '3':
                self.show_history()
            elif choice == '4':
                self.filter_by_type()
            elif choice == '5':
                self.filter_by_difficulty()
            elif choice == '6':
                self.save_current_history()
            elif choice == '7':
                self.clear_history()
            elif choice == '0':
                save_before_exit = input("Сохранить историю перед выходом? (y/n): ")
                if save_before_exit.lower() == 'y':
                    self.save_current_history()
                print("\nДо свидания! 👋")
                sys.exit(0)
            else:
                print("\n✗ Неверный выбор. Пожалуйста, выберите действие от 0 до 7.")

            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    app = RandomTaskGenerator()
    app.run()