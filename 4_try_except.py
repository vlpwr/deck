# Задача 1: Функция для безопасного деления
# Напишите функцию safe_division(a, b), которая выполняет деление числа a на число b и возвращает результат. Обработка исключения должна быть внутри функции.
# Если произойдет деление на ноль, обработайте исключение ZeroDivisionError и верните None.

def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# Примеры
print(safe_division(10, 2))
print(safe_division(10, 0))


# Задача 2: Функция для обработки нескольких исключений
# Напишите функцию multiple_exceptions_handling(key1, key2), которая работает со словарем:
# data = {"x": "10", "y": "0", "z": "abc"}
# Функция должна:
# Прочитать из словаря data значение по ключу key1, сконвертировать его в целое число.
# Прочитать из словаря data значение по ключу key2, сконвертировать его в целое число.
# Выполнить деление первого числа на второе.
# Обработка исключений:
#
# KeyError – если ключа нет в словаре.
# ValueError – если значение невозможно преобразовать в число.
# ZeroDivisionError – если происходит деление на ноль.
# Дополнительные требования:
#
# В каждом except блоке выводить соответствующее сообщение об ошибке.
# Использовать блок else, в котором вывести сообщение вида: *ошибок не возникло*
# Использовать блок finally, который выполнится в любом случае, можно добавить вывод сообщения.
# В конце функция должна возвращать результат деления или None, если возникло исключение.

def multiple_exceptions_handling(key1, key2):
    data = {"x": "10", "y": "0", "z": "abc"}

    try:
        num1 = int(data[key1])
        num2 = int(data[key2])
        result = num1 / num2

    except KeyError as e:
        print(f"KeyError: Ключ '{e}' не найден в словаре")
        result = None

    except ValueError as e:
        print(f"ValueError: Невозможно преобразовать значение в число: {e}")
        result = None

    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: Деление на ноль: {e}")
        result = None

    else:
        print("Ошибок не возникло")

    finally:
        print("Выполнение завершено")
        return result


# Примеры
print(multiple_exceptions_handling("x", "y"))
print(multiple_exceptions_handling("x", "z"))
print(multiple_exceptions_handling("x", "w"))
print(multiple_exceptions_handling("x", "x"))
