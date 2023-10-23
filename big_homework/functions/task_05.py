# Напишите функцию filter_negative_numbers, которая принимает список чисел, и возвращает новый список,
# составленный из элементов первого без отрицательных чисел,
# Пример:
# filter_negative_numbers([6, -5, 0, -1, 100]) -> [6, 0, 100]

def filter_negative_numbers(my_list: list[int | float]) -> list[int | float]:
    return [number for number in my_list if number >= 0]


assert filter_negative_numbers([6, -5, 0, -1, 100]) == [6, 0, 100]
