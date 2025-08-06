def sum_ignore_non_numbers(items):
    total = 0
    for el in items:
        if isinstance(el, (int, float)):
            total += el
    return total


def is_triangle(a, b, c):
    return a + b >= c and a + c >= b and b + c >= a


def average(*args):
    if not args:
        return 0
    else:
        return sum(args) / len(args)


def common_strings(list1, list2, ignore_case=True):
    new_list = []
    for word in list1:
        if ignore_case:
            word = word.lower()
        if word in list2:
            new_list.append(word.lower())
    return new_list


def upper_and_lower_case(string):
    result = ""
    for index, char in enumerate(string):
        if index % 2:
            result += char.lower()
        else:
            result += char.upper()
    return result


def pow(x, y):
    return x ** y
