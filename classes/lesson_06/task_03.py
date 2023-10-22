# Во всех задачах, где дан массив чисел - используйте функцию input_list чтобы получить этот массив от пользователя.
# Для тренировки предлагается сделать каждую задачу тремя способами: с помощью обычного цикла for, с помощью генератора списков, с помощью функции filter.
# 3.1 Дан список чисел. Удалите из него отрицательные числа.
# 3.2 Дан список чисел. Удалите из него нечётные числа.
# 3.3 Дан список чисел. Выведите три числа: количество положительных чисел, количество нулей, и количество отрицательных чисел. Используйте функции filter и len.
# 3.4 * Напишите свою реализацию функций my_filter, возвращающую список.
# 4.5 ** Напишите свою реализацию функций my_filter, которая вместо возвращения списка использует ключевое слово yield при генерации очередного элемента.

from task_01_1 import input_list_with_generator

input_list = input_list_with_generator()

# 3.1
output_list = []
for element in input_list:
    if element > 0:
        output_list.append(element)

print(f'3.1 с помощью обычного цикла for: {output_list}')
print(f'3.1 с помощью генератора списков: {[element for element in input_list if element > 0]}')
print(f'3.1 с помощью функции map: {list(filter(lambda element: element > 0, input_list))}')

# 3.2
output_list = []
for element in input_list:
    if element % 2 == 0:
        output_list.append(element)

print(f'3.2 с помощью обычного цикла for: {output_list}')
print(f'3.2 с помощью генератора списков: {[element for element in input_list if element % 2 == 0]}')
print(f'3.2 с помощью функции map: {list(filter(lambda element: element % 2 == 0, input_list))}')

# 3.3
output_list = [[], [], []]
for element in input_list:
    if element > 0:
        output_list[0].append(element)
    elif element < 0:
        output_list[1].append(element)
    else:
        output_list[2].append(element)

positive_count_with_generator = [element for element in input_list if element > 0]
zero_count_with_generator = [element for element in input_list if element == 0]
negative_count_with_generator = [element for element in input_list if element < 0]

positive_count_with_filter = len(list(filter(lambda element: element > 0, input_list)))
zero_count_with_filter = len(list(filter(lambda element: element == 0, input_list)))
negative_count_with_filter = len(list(filter(lambda element: element < 0, input_list)))

print(f'3.3 с помощью обычного цикла for: {len(output_list[0]), len(output_list[1]), len(output_list[2])}')
print(f'3.3: с помощью генератора списков: {positive_count_with_generator}, {zero_count_with_generator}, {negative_count_with_generator}')
print(f'3.3: с помощью функции filter: {positive_count_with_filter}, {zero_count_with_filter}, {negative_count_with_filter}')


# 3.4
def my_filter_simple_cycle(func, iterable):
    output_list = []
    for element in iterable:
        if func(element):
            output_list.append(element)
    return output_list


def my_filter_with_generator(func, iterable):
    return [element for element in iterable if func(element)]


print(f'3.4 с помощью обычного цикла for: {my_filter_simple_cycle(lambda element: element > 0, input_list)}')
print(f'3.4 с помощью генератора списков: {my_filter_with_generator(lambda element: element > 0, input_list)}')


# 3.5
def my_filter_gen_simple_cycle(func, iterable):
    for element in iterable:
        if func(element):
            yield element


def my_filter_gen_with_generator(func, iterable):
        yield [element for element in iterable if func(element)]


print(f'3.5 с помощью обычного цикла for: {list(my_filter_gen_simple_cycle(lambda element: element > 0, input_list))}')
print(f'3.5 с помощью генератора списков: {list(my_filter_gen_with_generator(lambda element: element > 0, input_list))}')
