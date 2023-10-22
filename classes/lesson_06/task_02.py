# Во всех задачах, где дан массив чисел - используйте функцию input_list чтобы получить этот массив от пользователя.
# Для тренировки предлагается сделать каждую задачу тремя способами: с помощью обычного цикла for, с помощью генератора списков, с помощью функции map.
# 2.1 Дан список чисел. Увеличьте каждый элемент в 100 раз.
# 2.2 Дан список чисел. Преобразуйте этот список в список строк.
# 2.3 Дан список чисел. Разделите каждый элемент на 100 и округлите до целого числа (функция round).
# 2.4 * Напишите свою реализацию функций my_map, возвращающую список.
# 2.5 ** Напишите свою реализацию функций my_map, которая вместо возвращения списка использует ключевое слово yield при генерации очередного элемента.

from task_01_1 import input_list_with_generator

input_list = input_list_with_generator()

# 2.1
output_list = []
for element in input_list:
    output_list.append(element * 100)

print(f'2.1 с помощью обычного цикла for: {output_list}')
print(f'2.1 с помощью генератора списков: {[element * 100 for element in input_list]}')
print(f'2.1 с помощью функции map: {list(map(lambda element: element * 100, input_list))}')

# 2.2
output_list = []
for element in input_list:
    output_list.append(str(element))

print(f'2.2 с помощью обычного цикла for: {output_list}')
print(f'2.2 с помощью генератора списков: {[str(element) for element in input_list]}')
print(f'2.2 с помощью функции map: {list(map(str, input_list))}')

# 2.3
output_list = []
for element in input_list:
    output_list.append(round(element / 100))

print(f'2.3 с помощью обычного цикла for: {output_list}')
print(f'2.3 с помощью генератора списков: {[round(element / 100) for element in input_list]}')
print(f'2.3 с помощью функции map: {list(map(lambda element: round(element / 100), input_list))}')


# 2.4
def my_map_simple_cycle(func, iterable):
    output_list = []
    for element in iterable:
        output_list.append(func(element))
    return output_list


def my_map_with_generator(func, iterable):
    return [func(element) for element in iterable]


print(f'2.4 с помощью обычного цикла for: {my_map_simple_cycle(lambda element: element+200, input_list)}')
print(f'2.4 с помощью генератора списков: {my_map_with_generator(lambda element: element+200, input_list)}')


# 2.5
def my_map_gen_simple_cycle(func, iterable):
    for element in iterable:
        yield func(element)


def my_map_gen_with_generator(func, iterable):
        yield [func(element) for element in iterable]


print(f'2.5 с помощью обычного цикла for: {list(my_map_gen_simple_cycle(lambda element: element+200, input_list))}')
print(f'2.5 с помощью генератора списков: {list(my_map_gen_with_generator(lambda element: element+200, input_list))}')
