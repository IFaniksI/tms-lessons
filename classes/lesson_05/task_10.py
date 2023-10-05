# Напишите функцию filter_odd_numbers, которая принимает на вход список целых чисел и возвращает новый список,
# состоящий из элементов первоначального, но без нечётных чисел.
# * Старайтесь использовать аннотации

def filter_odd_numbers(value: list[int]) -> list[int]:
    return [i for i in value if i % 2 == 0]


assert filter_odd_numbers([1, 2, 3, 4, 5]) == [2, 4]
assert filter_odd_numbers([1, 5, 4, 9, 2]) == [4, 2]
