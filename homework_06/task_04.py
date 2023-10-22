# Пользователь вводит произвольное количество слов через пробел.
# Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить, и возвращает строку,
# в которой все слова из списка соединены через символ разделитель.
# Пример ввода пользователя:
# hello this is my string
# @
# Вывод программы: hello@this@is@my@string
# Используйте функцию reduce.


from functools import reduce

input_list = input().split()
separator = input()


def my_join_with_simple_cycle(chars: list[str], sep: str) -> str:
    result = chars[0]
    for element in range(1, len(chars)):
        result += sep + chars[element]
    return result


def my_join_with_reduce(chars: list[str], sep: str) -> str:
    return reduce(lambda element_x, element_y: element_x + sep + element_y, chars)


print(f'с помощью обычного цикла for: {my_join_with_simple_cycle(input_list, separator)}')
print(f'с помощью функции reduce: {my_join_with_reduce(input_list, separator)}')