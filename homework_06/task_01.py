# Пользователь вводит произвольное количество латинских букв через пробел. Буквы могут быть как в верхнем,
# так и в нижнем регистре (на результат работы это влиять не должно).
# Напишите функцию map_to_tuples, которая принимает список из этих букв и возвращает список из кортежей.
# В каждом кортеже первой должна идти буква в верхнем регистре, а второй эта же буква в нижнем.
# Выведите результат работы функции на экран.
# Пример:
# Ввод пользователя: a B c
# Результат программы: [('A', 'a'), ('B', 'b'), ('C', 'c')]
# Используйте функции map, lower, upper

input_list = input().split()


def map_to_tuples_with_simple_cycle(value: list[str]) -> list[tuple]:
    result = []
    for element in value:
        result.append((element.upper(), element.lower()))
    return result


def map_to_tuples_with_generator(value: list[str]) -> list[tuple]:
    return [(element.upper(), element.lower()) for element in value]


def map_to_tuples_with_map(value: list[str]) -> list[tuple]:
    return list(map(lambda element: (element.upper(), element.lower()), value))


print(f'с помощью обычного цикла for: {map_to_tuples_with_simple_cycle(input_list)}')
print(f'с помощью генератора списков: {map_to_tuples_with_generator(input_list)}')
print(f'с помощью функции map: {map_to_tuples_with_map(input_list)}')
