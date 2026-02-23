# Задание 1. Вывода чисел от 1 до 10 с помощью цикла for
for i in range(1, 11):
    print(i)

# Задание 2. Вывода нечетных чисел от 1 до 20 с помощью цикла while
i = 0
while i <= 20:
    if i % 2 == 1:
        print(i)
    i += 1

# Задание 3. Суммирования чисел от 1 до n, используя цикл for
n = int(input("Введите число: "))
total_summ = 0
for i in range(1, n + 1):
    total_summ += i
print(total_summ)

# Задание 4. Считывания числа с клавиатуры и прекращения ввода при встрече числа 0
input_num = int(input("Введите число: "))

while input_num != 0:
    print(f"Вы ввели: {input_num}")
    input_num = int(input("Введите число: "))

# Задание 5. Вывода всех элементов списка, пропуская те, которые меньше 5
numbers = [1, 3, 5, 7, 2, 8]

for num in numbers:
    if num < 5:
        continue
    print(num)

# Задание 6. Подсчета суммы всех чётных чисел в списке
nums = [1, 2, 3, 4, 5, 6]

total = 0
for num in nums:
    if num % 2 == 0:
        total += num
print(total)

# Задание 7. Повторного запроса у пользователя слова и завершения цикла при вводе слова «стоп»
word = input("Введите слово: ")

while 'стоп' not in word:
    print(f"Вы ввели: {word}")
    word = input("Введите слово: ")

# Задание 8. Создания списка квадратов чисел от 1 до 10
squares = [i ** 2 for i in range(1, 11)]
print(squares)
