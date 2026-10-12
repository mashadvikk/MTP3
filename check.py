"""Проверка всех заданий: запускает doctest-примеры из docstring модулей.

Запуск: python check.py
"""
import doctest

import employees
import fibonacci
import figure
import json_store
import strtools

MODULES = [figure, strtools, fibonacci, json_store, employees]

if __name__ == "__main__":
    failed = 0
    total = 0
    for module in MODULES:
        result = doctest.testmod(module)
        failed += result.failed
        total += result.attempted
        status = "OK" if result.failed == 0 else "ОШИБКИ"
        print(f"{module.__name__:<10} примеров: {result.attempted:>2}  "
              f"{status}")
    print(f"Всего примеров: {total}, провалено: {failed}")
