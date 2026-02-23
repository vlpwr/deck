from functools import reduce
from collections import Counter


# 1. Квадраты через map
# Напишите функцию squares_map(nums), которая принимает список чисел и возвращает новый список их квадратов, используя map.
def squares_map(nums):
    return list(map(lambda x: x ** 2, nums))


print(squares_map([1, 2, 3, 4]))  # [1, 4, 9, 16]


# 2. Фильтрация чётных через filter
#  Напишите функцию filter_even(nums), которая принимает список чисел и возвращает список только чётных, используя filter.
def filter_even(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]


# 3. Сортировка слов через sorted и list.sort
# Напишите функцию, которая принимает список строк и возвращает его, отсортированный в алфавитном порядке. Реализуйте два варианта:#
# С помощью встроенной функции sorted — написать функцию sort_words_by_sorted_method(words)
# С помощью метода списка .sort() (не возвращает новый список, а меняет существующий) — написать функцию sort_words_by_sort_method(words)
def sort_words_by_sorted_method(words):
    return sorted(words)


def sort_words_by_sort_method(words):
    words_copy = words.copy()
    words_copy.sort()
    return words_copy


print(sort_words_by_sorted_method(["banana", "apple", "cherry"]))  # ['apple', 'banana', 'cherry']


# 4. Комбинация filter + map
# Напишите функцию square_odds(nums), которая сначала отбирает только нечётные числа (с помощью filter), а затем
# возвращает список их квадратов (с помощью map).
def square_odds(nums):
    odds = filter(lambda x: x % 2 != 0, nums)
    return list(map(lambda x: x ** 2, odds))


print(square_odds([1, 2, 3, 4, 5]))  # [1, 9, 25]


# 5. Накопление результата через functools.reduce
#  Напишите функцию product(nums), которая возвращает произведение всех чисел в списке, используя functools.reduce.

def product(nums):
    return reduce(lambda x, y: x * y, nums)


print(product([1, 2, 3, 4]))  # 24


# Методы строк и списков
# 6. Подсчёт слов через split и strip
# Напишите функцию count_words(text), которая принимает строку, убирает пробелы в начале и в конце (strip),
# разбивает её на слова (split) и возвращает количество слов.
def count_words(text):
    return len(text.strip().split())


print(count_words("  Hello, world! This is Python.  "))  # 5


# 7. Нормализация пробелов через split + join
# Напишите функцию normalize_whitespace(text), которая удаляет лишние пробелы между словами,
# приводя все последовательности пробелов к одному, используя split и join.
def normalize_whitespace(text):
    return ' '.join(text.split())


print(normalize_whitespace("This   is   a    test"))  # "This is a test"


# 8. Объединение слов в предложение через join
# Напишите функцию make_sentence(words), которая принимает список слов и собирает из них строку-предложение через пробел, используя join.
def make_sentence(words):
    return ' '.join(words)


print(make_sentence(["Python", "is", "fun"]))  # "Python is fun"


# 9. Расширение списка через extend и альтернативный вариант
# Напишите функцию, которая объединяет два списка. Реализуйте два варианта:
# С помощью метода extend — функция merge_lists_by_extend(a, b);
# Через оператор +, без использования extend — функция merge_lists_without_extend(a, b).
def merge_lists_by_extend(a, b):
    result = a.copy()
    result.extend(b)
    return result


def merge_lists_without_extend(a, b):
    return a + b


print(merge_lists_by_extend([1, 2], [3, 4]))  # [1, 2, 3, 4]


# 10. Удаление элементов через pop
# Напишите функцию pop_until_zero(nums), которая принимает список чисел и последовательно извлекает (pop) элементы с
# конца до тех пор, пока не встретит 0, и возвращает список извлечённых элементов (без самого нуля).
def pop_until_zero(nums):
    nums_copy = nums.copy()
    popped = []
    while nums_copy and nums_copy[-1] != 0:
        popped.append(nums_copy.pop())
    return popped


print(pop_until_zero([5, 3, 1, 0, 7, 8]))  # [8, 7]


# 11. Трансформация значений словаря через map + lambda
# Напишите функцию double_dict_values(d), которая принимает словарь d с числовыми значениями и возвращает новый словарь,
# в котором каждое значение умножено на 2. Используйте map вместе с lambda.
def double_dict_values(d):
    return dict(map(lambda item: (item[0], item[1] * 2), d.items()))


print(double_dict_values({'a': 1, 'b': 2, 'c': 3}))  # {'a': 2, 'b': 4, 'c': 6}


# 12. Фильтрация словаря через filter + lambda
# Напишите функцию filter_dict_by_value(d, threshold), которая принимает словарь d и число threshold, и возвращает
# новый словарь, содержащий только те пары, у которых значение больше threshold. Используйте filter вместе с lambda,
# а затем соберите результат обратно в словарь.
def filter_dict_by_value(d, threshold):
    return dict(filter(lambda item: item[1] > threshold, d.items()))


print(filter_dict_by_value({'x': 10, 'y': 3, 'z': 7}, 5))  # {'x': 10, 'z': 7}


# 13. Сортировка списка словарей через sorted + lambda
# Напишите функцию sort_people_by_age(people), где people — список словарей с ключами 'name' и 'age'. Функция должна возвращать новый список, отсортированный по полю 'age' по возрастанию, используя sorted с ключом-lambda.
def sort_people_by_age(people):
    return sorted(people, key=lambda p: p['age'])


people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Carol', 'age': 35}
]
print(sort_people_by_age(people))


# 14. Сортировка ключей и значений словаря через sorted
# Напишите две функции:
# sorted_dict_keys(d) — возвращает список ключей d в отсортированном порядке.
# sorted_dict_items_by_value(d) — возвращает список кортежей (key, value), отсортированных по значению, используя sorted.
def sorted_dict_keys(d):
    return sorted(d)


def sorted_dict_items_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])


d = {'b': 2, 'a': 1, 'c': 3}
print(sorted_dict_keys(d))  # ['a', 'b', 'c']
print(sorted_dict_items_by_value(d))  # [('a', 1), ('b', 2), ('c', 3)]


# 15. Комбинированное задание: map + filter + sorted
# Напишите функцию process_numbers(nums), которая:
# С помощью filter и lambda отбирает чётные числа.
# С помощью map и lambda возводит их в квадрат.
# Возвращает готовый список, отсортированный по убыванию, с помощью sorted(..., reverse=True).
def process_numbers(nums):
    evens = filter(lambda x: x % 2 == 0, nums)
    squares = map(lambda x: x ** 2, evens)
    return sorted(list(squares), reverse=True)


print(process_numbers([5, 2, 7, 4, 1, 8]))  # [64, 16, 4]


# 16. Подсчёт повторений слов через collections.Counter
# Напишите функцию count_word_frequencies(words), которая принимает список слов и возвращает словарь,
# где ключ — это слово, а значение — количество его повторений. Используйте collections.Counter.
def count_word_frequencies(words):
    return dict(Counter(words))


print(count_word_frequencies([
    "apple", "banana", "apple", "orange", "banana", "apple"
]))  # {'apple': 3, 'banana': 2, 'orange': 1}
