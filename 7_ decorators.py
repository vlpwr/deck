import time
import functools


# Задание 1: Декоратор для измерения времени выполнения функции
# Напишите декоратор, который измеряет и выводит время выполнения функции.
#
def time_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func.__name__} выполнилась за {end - start:.4f} сек")
        return result

    return wrapper


# Пример использования:
@time_logger
def example_function():
    time.sleep(3)


example_function()


# Задание 2: Декоратор для логирования вызовов функций
# Создайте декоратор, который будет логировать вызовы функции: выводить имя функции и переданные ей аргументы.

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат {func.__name__}: {result}")
        return result

    return wrapper


# Пример использования:
@log_calls
def example_function(a, b):
    return a + b


example_function(3, 5)


#
# Задание 3: Декоратор для кэширования результата функции
# Создайте декоратор, который будет кэшировать результат функции для заданных аргументов и возвращать
# сохранённый результат при повторных вызовах с теми же аргументами.

def cache_results(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print(f"Результат из кэша для {func.__name__}")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


# Пример использования:
@cache_results
def expensive_computation(x, y):
    print(f"Долгая вычислительная работа с {x}, {y}")
    time.sleep(1)
    return x * y


print(expensive_computation(2, 3))
print(expensive_computation(2, 3))
