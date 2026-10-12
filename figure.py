"""Задание 4 (средняя сложность): класс «Фигура» — площадь и периметр.

Базовый класс Figure знает только имя фигуры и объявляет методы area()
и perimeter(), а конкретные фигуры (круг, прямоугольник, треугольник)
наследуют его и считают каждая по своей формуле. Площадь треугольника
находится по формуле Герона, неправильный треугольник отклоняется.
"""
import math


class Figure:
    """Любая фигура: у неё есть имя, площадь и периметр."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Площадь фигуры. В базовом классе не определена."""
        raise NotImplementedError(
            f"для фигуры «{self.name}» формула площади не задана")

    def perimeter(self):
        """Периметр фигуры. В базовом классе не определён."""
        raise NotImplementedError(
            f"для фигуры «{self.name}» формула периметра не задана")

    def describe(self):
        """Строка с именем, площадью и периметром.

        >>> Rectangle(2, 5).describe()
        'Прямоугольник: площадь 10.00, периметр 14.00'
        """
        return (f"{self.name}: площадь {self.area():.2f}, "
                f"периметр {self.perimeter():.2f}")


class Circle(Figure):
    """Круг по радиусу.

    >>> round(Circle(2).area(), 2)
    12.57
    >>> round(Circle(2).perimeter(), 2)
    12.57
    >>> Circle(-1)
    Traceback (most recent call last):
    ...
    ValueError: радиус не может быть отрицательным
    """

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("радиус не может быть отрицательным")
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Figure):
    """Прямоугольник по двум сторонам.

    >>> Rectangle(3, 4).area()
    12
    >>> Rectangle(3, 4).perimeter()
    14
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("стороны должны быть положительными")
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Figure):
    """Треугольник по трём сторонам, площадь — по формуле Герона.

    >>> Triangle(3, 4, 5).area()
    6.0
    >>> Triangle(3, 4, 5).perimeter()
    12
    >>> Triangle(1, 1, 5)
    Traceback (most recent call last):
    ...
    ValueError: такого треугольника не существует
    """

    def __init__(self, a, b, c):
        sides = sorted((a, b, c))
        if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
            raise ValueError("такого треугольника не существует")
        super().__init__("Треугольник")
        self.a, self.b, self.c = a, b, c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    figures = [Circle(5), Rectangle(3, 7), Triangle(3, 4, 5)]
    for figure in figures:
        print(figure.describe())
