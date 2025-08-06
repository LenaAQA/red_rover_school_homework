"""
1
Регистрация (часть 1)
1.	Напишите функцию registration(), которая принимает 2 аргумента - username (строка) и password() (строка)

.	Функция должна проверить username, а именно: username является строкой.
.	Длина этой строки минимум 4 символа и максимум 15.
.	Username состоит только из букв.
.
.	Если username некорректный, то функция должна вызвать исключение ValueError.
.	Функция должна проверить password, а именно: password является строкой.
.	Длина этой строки минимум 8 символов и максимум 45.
.	Password состоит только из букв и цифр.
.
.	Если password некорректный, то функция должна вызвать исключение ValueError.
.	Если “регистрация” прошла успешно, то функция должна вернуть True.

Дополнительно: создайте свой тип исключения RegistrationError и используйте его вместо ValueError.
"""


def registration(username, password):
    if not isinstance(username, str) and 4 <= len(username) <= 15 and username.isalpha():
        raise ValueError
    if not isinstance(password, str) and 8 <= len(password) <= 45 and password.isalnum():
        raise ValueError

    return True


class RegistrationError(Exception):
    pass


def registration_two(username, password):
    if not isinstance(username, str) and 4 <= len(username) <= 15 and username.isalpha():
        raise RegistrationError("Некорректный username!")
    if not isinstance(password, str) and 8 <= len(password) <= 45 and password.isalnum():
        raise RegistrationError("Некорректный password!")

    return True


"""
 Регистрация (часть 2)
Напишите программу, которая в бесконечном цикле запрашивает у пользователя ввести логин и пароль
и сохраняет их в соответствующие переменные.
Вызовите функцию registration из предыдущей задачи передав ей введенные логин и пароль пользователя.
Если в registration были переданы некорректные данные, то ваша программа должна перехватить вызванное функцией
исключение RegistrationError и написать в консоль “Ошибка регистрации!”,
 а затем снова попросить пользователя ввести данные.
Если данные были введены корректно, то программа должна вывести “Успешно!” и выйти из бесконечного цикла.
"""


class RegistrationError(Exception):
    pass


def registration(username, password):
    if not isinstance(username, str) and 4 <= len(username) <= 15 and username.isalpha():
        raise RegistrationError("Некорректный username!")

    if not isinstance(password, str) and 8 <= len(password) <= 45 and password.isalnum():
        raise RegistrationError("Некорректный password!")

    return True


while True:
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    try:
        registration(username, password)
        print("Успешно!")
        break
    except RegistrationError:
        print("Ошибка регистрации!")

"""
Дорогой дневник... 
Создайте пустой текстовый файл journal.txt 
Программа должна в бесконечном цикле запрашивать пользователя ввести строку, 
которая является одним из режимов: “прочитать”, “записать”, “выйти”. 
•	Если пользователь ввел “записать”: Программа просит пользователя ввести еще одну строку, 
которая будет записана в файл. 
•	Программа дозаписывает эту строку в файл journal.txt c новой строки. 
•	
•	Если пользователь ввел “прочитать”: Программа выводит на экран все содержимое файла journal.txt. 
•	
•	Если пользователь ввел “выйти”: Программа пишет в консоль “Еще увидимся!”, 
выходит из бесконечного цикла и завершается. 
•	
•	Если пользователь ввел что-то другое: Программа ничего не делает, просто возвращается к следующей итерации 
бесконечного цикла. 
"""

while True:
    string = input("Введите строку: ")
    if string == "записать":
        message = input(f"Введите сроку для записи в файл: ")
        with open("journal.txt", "a", encoding="utf-8") as file:
            file.write(f"{message}\n")
    elif string == "прочитать":
        with open("journal.txt", "r", encoding="utf-8") as file:
            print(file.read())
    elif string == "выйти":
        print("Еще увидимся!")
        break
