"""Задание 9 (повышенная сложность): абстрактный класс через abc.

Employee — абстрактный класс: сам по себе «сотрудник вообще»
существовать не может, зарплата считается только у конкретных
должностей. Метод monthly_salary() помечен @abstractmethod, поэтому
наследник без него просто не создастся, а общий метод info()
достаётся всем готовым.
"""
from abc import ABC, abstractmethod


class Employee(ABC):
    """Абстрактный сотрудник: имя и ставка, зарплата — у наследников."""

    def __init__(self, name, base_rate):
        if base_rate < 0:
            raise ValueError("ставка не может быть отрицательной")
        self.name = name
        self.base_rate = base_rate

    @abstractmethod
    def monthly_salary(self):
        """Зарплата за месяц. Считается у каждой должности по-своему."""

    def info(self):
        """Общий для всех метод: имя и посчитанная зарплата."""
        return f"{self.name}: {self.monthly_salary():.0f} руб./мес"


class Manager(Employee):
    """Менеджер: ставка плюс премия за каждого подчинённого.

    >>> Manager("Ольга", 80000, subordinates=5).monthly_salary()
    95000
    """

    def __init__(self, name, base_rate, subordinates=0, per_head=3000):
        super().__init__(name, base_rate)
        self.subordinates = subordinates
        self.per_head = per_head

    def monthly_salary(self):
        return self.base_rate + self.subordinates * self.per_head


class Developer(Employee):
    """Разработчик: ставка умножается на коэффициент грейда.

    >>> Developer("Инна", 100000, grade=1.5).monthly_salary()
    150000.0
    """

    def __init__(self, name, base_rate, grade=1.0):
        super().__init__(name, base_rate)
        self.grade = grade

    def monthly_salary(self):
        return self.base_rate * self.grade


class Intern(Employee):
    """Стажёр: фиксированная стипендия, не зависящая от ставки.

    >>> Intern("Катя", 50000).monthly_salary()
    15000
    """

    STIPEND = 15000

    def monthly_salary(self):
        return self.STIPEND


if __name__ == "__main__":
    staff = [
        Manager("Ольга Смирнова", 80000, subordinates=4),
        Developer("Инна Ветрова", 100000, grade=1.3),
        Intern("Катя Морозова", 50000),
    ]
    for person in staff:
        print(person.info())
    try:
        Employee("Без Должности", 40000)
    except TypeError:
        print("Создать «просто сотрудника» нельзя: Employee абстрактный.")
