import random


# Задание 1: Функция для проверки числа на простоту
def is_simple(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Задание 2: Функция для вычисления наибольшего общего делителя (НОД)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Задание 3: Функция для реверса строки
def reverse_string(s):
    return s[::-1]


# def reverse_string(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result

# Задание 4: Функция для генерации списка случайных чисел
def generate_random_list(n, start, end):
    result = []
    for _ in range(n):
        result.append(random.randint(start, end))
    return result
