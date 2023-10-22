# Во всех задачах, где дан массив чисел - используйте функцию input_list чтобы получить этот массив от пользователя.
# Для тренировки предлагается сделать каждую задачу двумя способами: с помощью обычного цикла for и с помощью функции reduce.
# 4.1 Дан список чисел. Найти его сумму.
# 4.2 Дан список чисел. Найти минимальное число.
# 4.3 Дан список чисел. Найти произведение всех элементов.
# 4.4 С помощью функции reduce и range найти факториал числа 5.
# 4.5 * Напишите свою реализацию функции my_reduce. Для простоты можно сделать третий параметр обязательным.

from task_01_1 import input_list_with_generator
from functools import reduce

input_list = input_list_with_generator()

# 4.1
result = 0
for element in input_list:
    result += element

print(f'4.1 с помощью обычного цикла: {result}')
print(f'4.1 с помощью функции reduce: {reduce(lambda element, value: element + value, input_list)}')

# 4.2
for element in input_list:
    if element <= input_list[0]:
        result = element

print(f'4.2 с помощью обычного цикла: {result}')
print(f'4.2 с помощью функции reduce: {reduce(lambda element, value: min(element, value), input_list)}')

# 4.3
result = 1
for element in input_list:
    result *= element

print(f'4.3 с помощью обычного цикла: {result}')
print(f'4.3 с помощью функции reduce: {reduce(lambda element, value: element * value, input_list)}')

# 4.4
result = 1
for element in range(1, 6):
    result *= element

print(f'4.4 с помощью обычного цикла: {result}')
print(f'4.4 с помощью функции reduce: {reduce(lambda element, value: element * value, range(1, 6))}')


# 4.5
def my_reduce_gen_simple_cycle(func, iterable, value=1):
    result = value
    for element in iterable:
        result = func(result, element)
    return result


print(f'4.5 с помощью обычного цикла: {my_reduce_gen_simple_cycle(lambda element, value: element * value, range(1, 6))}')
