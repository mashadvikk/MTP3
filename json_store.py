"""Задание 5 (повышенная сложность): сериализация объектов в JSON.

JsonSerializer превращает объект в JSON-строку и обратно, умеет
сохранять в файл и загружать оттуда. Чтобы объект сериализовался,
у него должны быть методы to_dict() и from_dict() — дальше сериализатору
ничего о нём знать не надо. Кириллица сохраняется как есть
(ensure_ascii=False), файл пишется в UTF-8.
"""
import json
import os


class JsonSerializer:
    """Сериализация объектов в JSON и обратно."""

    @staticmethod
    def to_json(obj):
        """Объект -> JSON-строка.

        >>> JsonSerializer.to_json(Movie("Девчата", 1961, "Чулюкин"))
        '{"title": "Девчата", "year": 1961, "director": "Чулюкин"}'
        """
        return json.dumps(obj.to_dict(), ensure_ascii=False)

    @staticmethod
    def from_json(text, cls):
        """JSON-строка -> объект класса cls.

        >>> text = ('{"title": "Кавказская пленница", "year": 1967, '
        ...         '"director": "Гайдай"}')
        >>> JsonSerializer.from_json(text, Movie)
        Movie('Кавказская пленница', 1967, 'Гайдай')
        """
        return cls.from_dict(json.loads(text))

    @staticmethod
    def list_to_json(items):
        """Список объектов -> JSON-строка со списком словарей.

        >>> JsonSerializer.list_to_json([Movie("Мимино", 1977, "Данелия")])
        '[{"title": "Мимино", "year": 1977, "director": "Данелия"}]'
        """
        return json.dumps([item.to_dict() for item in items],
                          ensure_ascii=False)

    @staticmethod
    def list_from_json(text, cls):
        """JSON-строка со списком -> список объектов."""
        return [cls.from_dict(item) for item in json.loads(text)]

    @staticmethod
    def save(obj, filename):
        """Сохраняет объект в файл в кодировке UTF-8."""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(JsonSerializer.to_json(obj))

    @staticmethod
    def load(filename, cls):
        """Загружает объект из файла."""
        with open(filename, encoding="utf-8") as file:
            return JsonSerializer.from_json(file.read(), cls)


class Movie:
    """Фильм: название, год и режиссёр. Умеет to_dict/from_dict."""

    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director

    def to_dict(self):
        return {"title": self.title, "year": self.year,
                "director": self.director}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["year"], data["director"])

    def __eq__(self, other):
        return (isinstance(other, Movie)
                and self.to_dict() == other.to_dict())

    def __repr__(self):
        return f"Movie({self.title!r}, {self.year!r}, {self.director!r})"


if __name__ == "__main__":
    film = Movie("Ирония судьбы", 1975, "Рязанов")
    text = JsonSerializer.to_json(film)
    print("В JSON:", text)
    restored = JsonSerializer.from_json(text, Movie)
    print("Обратно в объект:", restored)
    print("Совпал с исходным:", restored == film)
    filename = "movie.json"
    JsonSerializer.save(film, filename)
    print("Из файла:", JsonSerializer.load(filename, Movie))
    os.remove(filename)
