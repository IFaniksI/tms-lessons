# Напишите функцию get_natural_numbers, которое принимает целое число n
# и возвращает список натуральных чисел от 1 до n включительно. Используйте генераторы списков.


def get_natural_numbers(n):
    return [i for i in range(1, n + 1)]


assert get_natural_numbers(4) == [1, 2, 3, 4]
assert get_natural_numbers(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
