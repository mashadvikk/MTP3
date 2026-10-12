"""Задание 6 (средняя сложность): класс со статическими методами.

TextHelper — набор приёмов для работы со строками. Объект создавать
не нужно: методы объявлены через @staticmethod и вызываются прямо
с класса, как TextHelper.is_palindrome(...).
"""


class TextHelper:
    """Статические методы для разбора текста."""

    VOWELS = "аеёиоуыэюя"

    @staticmethod
    def is_palindrome(text):
        """True, если текст читается одинаково в обе стороны.

        Регистр букв, пробелы и знаки препинания не учитываются.

        >>> TextHelper.is_palindrome("А роза упала на лапу Азора")
        True
        >>> TextHelper.is_palindrome("Казак")
        True
        >>> TextHelper.is_palindrome("привет")
        False
        >>> TextHelper.is_palindrome("")
        True
        """
        letters = [ch.lower() for ch in text if ch.isalpha()]
        return letters == letters[::-1]

    @staticmethod
    def vowel_count(text):
        """Сколько гласных букв в тексте.

        >>> TextHelper.vowel_count("мама")
        2
        >>> TextHelper.vowel_count("Рысь")
        1
        >>> TextHelper.vowel_count("")
        0
        """
        return sum(1 for ch in text.lower() if ch in TextHelper.VOWELS)

    @staticmethod
    def reverse_words(text):
        """Меняет порядок слов в строке на обратный.

        >>> TextHelper.reverse_words("мама мыла раму")
        'раму мыла мама'
        >>> TextHelper.reverse_words("один")
        'один'
        """
        return " ".join(reversed(text.split()))

    @staticmethod
    def summary(text):
        """Мини-отчёт о строке: слова, гласные, палиндром ли.

        >>> TextHelper.summary("Казак")
        'слов: 1, гласных: 2, палиндром: да'
        """
        words = len(text.split())
        vowels = TextHelper.vowel_count(text)
        pal = "да" if TextHelper.is_palindrome(text) else "нет"
        return f"слов: {words}, гласных: {vowels}, палиндром: {pal}"


if __name__ == "__main__":
    phrases = ["А роза упала на лапу Азора", "Методы и технологии"]
    for phrase in phrases:
        print(f"«{phrase}» — {TextHelper.summary(phrase)}")
    print("Задом наперёд:", TextHelper.reverse_words("лаба три готова"))
