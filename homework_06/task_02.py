# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
# Пример:
# Ввод пользователя: a b c d e f
# Результат программы: ['b', 'c', 'd', 'f']
# Используйте функцию filter.
# Список всех гласных английского языка: a, e, i, o, u

input_list = input().split()
vowels = ['a', 'e', 'i', 'o', 'u']


def remove_vowels_with_simple_cycle(chars):
    result = []
    for element in chars:
        if element not in vowels:
            result.append(element)
    return result


def remove_vowels_with_generator(chars):
    return [element for element in chars if element not in vowels]


def remove_vowels_with_filter(chars):
    return list(filter(lambda element: element not in vowels, chars))


print(f'с помощью обычного цикла for: {remove_vowels_with_simple_cycle(input_list)}')
print(f'с помощью генератора списков: {remove_vowels_with_generator(input_list)}')
print(f'с помощью функции map: {remove_vowels_with_filter(input_list)}')