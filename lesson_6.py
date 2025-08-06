"""
1
Модуль.
-	Перенесите ваши функции из прошлого домашнего задания в отдельный файл и
импортируйте их в основной (исполняемый) файл.
-	Запустите каждую вашу функцию по 1 или более раз в исполняемом файле.
"""
import lesson_6_function

print(lesson_6_function.sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))

print(lesson_6_function.is_triangle(2, 4, 9))
print(lesson_6_function.is_triangle(3, 4, 5))

print(lesson_6_function.average(1, 2, 3, 4, 5, 6, 7, 8))
print(lesson_6_function.average())

fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
print(lesson_6_function.common_strings(fruits_1, fruits_2))
print(lesson_6_function.common_strings(fruits_1, fruits_2, False))

print(lesson_6_function.upper_and_lower_case(input("Введите текст: ")))

"""
2
Анонимная функция 🎭.
-	Создайте анонимную функцию pow, которая принимает 2 аргумента x и y.
Функция должна возвращать x, возведенное в степень y.
"""

from lesson_6_function import pow as p

print(p(3, 2))

"""
3
Змея 🐍.
-	Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
-	Функция должна создать новую строку, где все гласные буквы aeiouyAEIOUY в строке text дублируются.
-	Например, такой вызовы функции snake_talk(“Harry”) должен вернуть строку “Haaryy”.
"""


def snake_talk(text):
    str = ""
    for letter in text:
        if letter in "aeiouyAEIOUY":
            str += letter * 2
        else:
            str += letter
    return str


print(snake_talk("gfeeffako"))
print(snake_talk("Harry"))
