# Задание 1: Функция sum_all
# Напишите функцию sum_all(*args), которая принимает произвольное количество чисел и возвращает их сумму.
# Напишите ещё одну функцию sum_all_modified так, чтобы она возвращала не только сумму, но и количество переданных аргументов.

def sum_all(*args):
    return sum(args)


def sum_all_modified(*args):
    return sum(args), len(args)


print(sum_all(1, 2, 3, 4))
print(sum_all_modified(1, 2, 3, 4))


# Задание 2: Функция greet
# Напишите функцию greet(**kwargs), которая принимает произвольное количество именованных аргументов (ключ-значение) и выводит сообщение с использованием этих данных.
def greet(**kwargs):
    message = "Привет! Вот твои данные: "
    for key, value in kwargs.items():
        message += f"{key}={value}, "
    print(message.rstrip(", "))


def greet_modified(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello!")


greet_modified(name="John", age=30, city="New York")  # Ожидаемый результат: "Hello, John!"
greet_modified(age=30, city="New York")  # Ожидаемый результат: "Hello!"
