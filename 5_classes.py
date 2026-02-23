# Задание 1: Класс Car
# Создайте класс Car.
# У класса должно быть несколько атрибутов, например:
# brand (марка);
# model (модель);
# year (год выпуска);
# color (цвет);
# engine_started (логическое значение: запущен двигатель или нет).

class Car:

    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_started = False

    # Определите в классе методы:
    # start_engine(): запускает двигатель (выставляет engine_started в True).
    def start_engine(self):
        self.engine_started = True

    # stop_engine(): глушит двигатель (выставляет engine_started в False).
    def stop_engine(self):
        self.engine_started = False

    # print_info(): выводит (печатает) на экран информацию об автомобиле (марка, модель, цвет и состояние двигателя).
    def print_info(self):
        status = "запущен" if self.engine_started else "остановлен"
        print(f"{self.brand} {self.model}, {self.year}г., {self.color}, двигатель: {status}")


# Создайте несколько экземпляров (объектов) класса Car, присвоив разные значения атрибутам.
# Для каждого экземпляра:
# Вызовите метод print_info() до запуска двигателя, чтобы проверить текущее состояние.
# Затем запустите двигатель методом start_engine() и снова выведите информацию, чтобы убедиться, что состояние изменилось.
# Остановите двигатель методом stop_engine() и ещё раз выведите информацию.

car1 = Car("Toyota", "Camry", 2020, "черный")

car1.print_info()  # до запуска
car1.start_engine()
car1.print_info()  # после запуска
car1.stop_engine()
car1.print_info()  # после остановки

car2 = Car("BMW", "X5", 2022, "белый")
car2.print_info()
car2.start_engine()
car2.print_info()


# Задание 2: Класс Rectangle
# Написать класс Rectangle (прямоугольник), чтобы иметь возможность сравнивать экземпляры этого класса по площади.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width * self.height == other.width * other.height

    def __lt__(self, other):
        return self.width * self.height < other.width * other.height

    def __le__(self, other):
        return self.width * self.height <= other.width * other.height


rectangle1 = Rectangle(1, 1)
rectangle2 = Rectangle(2, 2)
rectangle3 = Rectangle(2, 2)
print(rectangle1 == rectangle2)  # False
print(rectangle2 == rectangle3)  # True
print(rectangle1 < rectangle2)  # True
print(rectangle2 < rectangle3)  # False
print(rectangle2 <= rectangle3)  # True
