"""
1
Прямоугольник
-	Создайте класс Rectangle, который принимает ширину и высоту прямоугольника при создании
и должен иметь соответствующие атрибуты width и height (целые числа).
-	Создайте метод area(), который возвращает площадь прямоугольника.
-	Создайте метод perimeter(), который возвращает периметр прямоугольника.
Пример:
rect = Rectangle(2, 4)
a = rect.area() # Вернул 8
p = rect.perimeter() # Вернул 12
"""


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


rectangle = Rectangle(2, 4)
a = rectangle.area()
p = rectangle.perimeter()
print(a, p)

"""
2
Автомобиль
-	Создайте класс Car, который принимает марку автомобиля (make) в виде строки и максимально возможную скорость 
(max_speed) в виде целого числа при создании. Также при инициализации (в теле __init__) экземпляра Car 
должен быть автоматически создан атрибут speed, равный 0 (текущая скорость автомобиля).

-	Создайте метод display_speed(), который выводит в консоль текущую скорость автомобиля. 
-	Создайте метод accelerate(), который увеличивает скорость автомобиля на 10, при этом скорость автомобиля 
не должна превышать max_speed, если вызывается accelerate() при максимальной скорости, 
то скорость не должна увеличиваться. 
-	Создайте метод brake(), который уменьшает скорость автомобиля на 10, при этом 
скорость автомобиля не может быть меньше 0. Если вызывается метод brake() при скорости равной 0, 
то скорость не должна уменьшаться. 
Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 3
"""


class Car:
    def __init__(self, m, max):
        self.make = m
        self.max_speed = max
        self.speed = 0

    def display_speed(self):
        return print(f"Текущая скорость: {self.speed}")

    def accelerate(self):
        self.speed += 10
        if self.speed >= self.max_speed:
            return print(f"Достигнута максимальная скорость: {self.max_speed}")

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            return self.speed


my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed()
