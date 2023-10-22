# Напишите функцию input_list, которая не принимает входных аргументов, а просто читает строку,
# которую ввёл пользователь (вызывая функцию input), разбивает её по пробелам (с помощью функции split),
# и возвращает список целых чисел.


# с помощью обычного цикла
def input_list_with_simple_cycle() -> list[int]:
    input_strings = input().split()
    output_numbers = []
    for element in input_strings:
        output_numbers.append(int(element))
    return output_numbers


# с помощью генератора списков
def input_list_with_generator() -> list[int]:
    return [int(element) for element in input().split()]


# с помощью функции map
def input_list_with_map() -> list[int]:
    return list(map(int, input().split()))
