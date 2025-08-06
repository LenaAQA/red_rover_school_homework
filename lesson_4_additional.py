"""
Магазин.
Есть словарь с товарами:
products = {"apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk":{"quantity": 12, "price": 90},
     "bread": {"quantity": 30, "price": 40}}
-	Необходимо увеличить цену всех продуктов на 20 процентов.
-	Удалить товар “milk”.
-	Добавить товар “salt” с количеством 7 и ценой 12.
-	Вывести общую стоимость всех товаров в магазине.
Ответ: 6516.0
"""

products = {"apple": {"quantity": 10, "price": 100}, "banana": {"quantity": 20, "price": 50},
            "orange": {"quantity": 15, "price": 80}, "grape": {"quantity": 8, "price": 120},
            "milk": {"quantity": 12, "price": 90}, "bread": {"quantity": 30, "price": 40}}

for value in products.values():
    value["price"] *= 1.2

del products["milk"]
products["salt"] = {"quantity": 7, "price": 12}

total_cost = 0
for value in products.values():
    total_cost += value["price"] * value["quantity"]

print(total_cost)

"""
2 Alice.
Есть два списка одинаковой длины:

keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']

values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 
'Masters in Computer Science', 'TechCorp', 90000]

-	Создайте словарь info из ключей keys и значений values. 
(Каждое значение занимает ту же позицию, что и ключ в другом списке)
-	Выведите словарь info на экран.
"""

keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']

values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading',
          'Masters in Computer Science', 'TechCorp', 90000]
info = dict(zip(keys, values))
print(info)

keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']

values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading',
          'Masters in Computer Science', 'TechCorp', 90000]
info = {}
for i in range(len(keys)):
    info[keys[i]] = values[i]
print(info)

"""
3
Шифр.
Есть сообщение (строка):
"2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя" 
И ключ к шифру, где каждую букву нужно заменить на ее значение в словаре: 
cipher = {
    "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
    "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
    "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
    "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
    "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}
-	Расшифруйте секретное сообщение с помощью ключа cipher, при этом мусорные значение (которых нет в словаре) 
должны быть пропущены и не добавлены в результат.
-	Выведите результат на экран.
-	Дополнительно: напишите программу, которая получает строку через ввод с клавиатуры и “отправляет” 
зашифрованный ответ агенту. 
"""

message = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
cipher = {
    "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
    "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
    "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
    "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
    "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}
secret_message = ""
for letter in message:
    if letter in cipher:
        secret_message += cipher[letter]

print(secret_message)

cipher = {
    "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
    "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
    "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
    "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
    "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}

new_cipher = {}
for key, value in cipher.items():
    new_cipher[value] = key
message = input()
encrypted_message = ""

for i in message:
    if i in new_cipher:
        encrypted_message += new_cipher[i]

print(encrypted_message)

"""
4
Самая популярная буква.
Есть строка: dialog = "Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.
Doc: Вес тут совершенно ни при чем. "
# Тройные кавычки позволяют удобно писать текст в несколько строк.
-	С помощью словаря подсчитайте количество букв в строке dialog игнорируя регистр. 
Ключами в словаре должны быть буквы, а значения - количество вхождения буквы в текст. Например: {'т': 26, 'е': 32...}
-	Вывести на экран букву, которая встречается максимальное количество раз.
"""

dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.
Doc: Вес тут совершенно ни при чем. """

dict = {}

alphabet_dict = {chr(letter): 0 for letter in range(ord('а'), ord('я') + 1)}
alphabet_dict['ё'] = 0

for letter in dialog.lower():
    if letter.isalpha() and letter in alphabet_dict:
        alphabet_dict[letter] += 1

print(alphabet_dict)
print(max(alphabet_dict, key=alphabet_dict.get))
