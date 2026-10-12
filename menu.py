"""Главное меню: запуск любого задания лабораторной №3 (вариант 4)."""
import subprocess
import sys

TASKS = {
    "1": ("Средняя 4. Класс «Фигура»", "figure.py"),
    "2": ("Средняя 6. Статические методы", "strtools.py"),
    "3": ("Средняя 10. Класс-итератор", "fibonacci.py"),
    "4": ("Повышенная 5. Сериализация в JSON", "json_store.py"),
    "5": ("Повышенная 9. Абстрактный класс", "employees.py"),
}


def main():
    while True:
        print("\nЛабораторная №3, вариант 4. Задания:")
        for key, (title, _) in TASKS.items():
            print(f"  {key}. {title}")
        print("  0. Выход")
        choice = input("Номер задания: ").strip()
        if choice == "0":
            print("Пока!")
            return
        task = TASKS.get(choice)
        if task is None:
            print("Нет такого пункта, попробуйте ещё раз.")
            continue
        title, script = task
        print(f"--- {title} ---")
        subprocess.run([sys.executable, script], check=False)


if __name__ == "__main__":
    main()
