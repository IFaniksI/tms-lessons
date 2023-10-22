# * Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
# Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.
# Пример:
# Ввод пользователя: a B c d E F
# Результат программы: ['B', 'c', 'd', 'F']
# Используйте функцию filter.

input_list = input().split()
vowels = ['a', 'e', 'i', 'o', 'u']


def remove_vowels_with_simple_cycle(chars: list[str]) -> list[str]:
    result = []
    for element in chars:
        if element.lower() not in vowels:
            result.append(element)
    return result


def remove_vowels_with_generator(chars: list[str]) -> list[str]:
    return [element for element in chars if element.lower() not in vowels]


def remove_vowels_with_filter(chars: list[str]) -> list[str]:
    return list(filter(lambda element: element.lower() not in vowels, chars))


print(f'с помощью обычного цикла for: {remove_vowels_with_simple_cycle(input_list)}')
print(f'с помощью генератора списков: {remove_vowels_with_generator(input_list)}')
print(f'с помощью функции filter: {remove_vowels_with_filter(input_list)}')