"""Задание 10 (средняя сложность): класс-итератор.

Fibonacci реализует протокол итератора: метод __iter__ возвращает сам
объект, а __next__ выдаёт очередное число Фибоначчи и бросает
StopIteration, когда числа перевалили за границу. Поэтому объект можно
отдавать прямо в цикл for и в list().
"""


class Fibonacci:
    """Итератор по числам Фибоначчи, не превышающим границу limit.

    >>> list(Fibonacci(30))
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    >>> list(Fibonacci(1))
    [0, 1, 1]
    >>> list(Fibonacci(0))
    [0]
    >>> list(Fibonacci(-5))
    []
    """

    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        self.next_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        pair_sum = value + self.next_value
        self.current, self.next_value = self.next_value, pair_sum
        return value

    def sum(self):
        """Сумма всех чисел до границы (сбрасывает итератор).

        >>> Fibonacci(30).sum()
        54
        """
        total = 0
        for number in self:
            total += number
        return total


class EvenRange:
    """Итератор по чётным числам от 0 до n включительно.

    >>> list(EvenRange(9))
    [0, 2, 4, 6, 8]
    >>> list(EvenRange(1))
    [0]
    """

    def __init__(self, n):
        self.n = n
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.n:
            raise StopIteration
        value = self.number
        self.number += 2
        return value


if __name__ == "__main__":
    border = 100
    numbers = list(Fibonacci(border))
    print(f"Числа Фибоначчи до {border}: {numbers}")
    print(f"Их сумма: {Fibonacci(border).sum()}")
    print(f"Чётные до 20: {list(EvenRange(20))}")
