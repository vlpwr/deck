import time
from contextlib import contextmanager


# Задание 1: Создание простого контекстного менеджера
# Напишите свой собственный контекстный менеджер, который будет открывать и закрывать файл для записи.
# Используйте методы класса __enter__ и __exit__.

class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# Пример использования:
with FileWriter('example.txt') as file:
    file.write("Hello, World!")


# Задание 2: Контекстный менеджер через contextlib
# Используйте библиотеку contextlib для создания контекстного менеджера, который будет отслеживать время выполнения блока кода и распечатывать его.
#
@contextmanager
def time_tracker():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Время выполнения: {end - start:.2f} секунд")


# Пример использования:
with time_tracker():
    # Выполнение кода
    time.sleep(1)
