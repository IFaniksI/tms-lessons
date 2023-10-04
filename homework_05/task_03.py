# Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список,
# состоящий из их квадратов. То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*args):
    return [i ** 2 for i in args]


assert generate_squares(2, 3, 4) == [4, 9, 16]
assert generate_squares(4, -7, 56) == [16, 49, 3136]
assert generate_squares(0, 59, -78, -100, 3) == [0, 3481, 6084, 10000, 9]
