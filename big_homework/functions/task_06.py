# Скопируйте функции прошлых 5 заданий в один файл.
# Напишите программу, которая спрашивает у пользователя номер задачи, решение которой он хочет проверить,
# пользователь вводит число от 1 до 5, в зависимости от выбранного номера
# запросите у пользователя входные данные для задачи (если это нужно) и выведите ответ.
# Примеры:
# Введите номер задачи: 1
# Hello world!
#
# Введите номер задачи: 2
# Введите первое число: 100
# Введите второе число: 200
# Сумма чисел: 300
#
# Введите номер задачи: 3
# Введите первое число: 100
# Введите второе число: 200
# Первое число меньше второго? Ответ: True
#
# Введите номер задачи: 4
# Введите первое число: 200
# Введите второе число: 100
# Результат сравнения: 1
#
# Введите номер задачи: 5
# Введите числа, разделённые пробелов: 1 -1 100 0 -12 5
# Мы удалили отрицательные числа из вашего списка: [1, 100, 0, 5]
#
# Введите номер задачи: 700
# Задачи с таким номером нет.

def hello_world():
    print('Hello world!')


def my_sum(x: int | float, y: int | float) -> int | float:
    return x + y


def simple_compare(x: int | float, y: int | float) -> bool:
    return x < y


def compare(x: int | float, y: int | float) -> int:
    return -1 if x < y else 1 if x > y else 0


def filter_negative_numbers(my_list: list[int | float]) -> list[int | float]:
    return [number for number in my_list if number >= 0]


input_number = int(input('Введите номер задачи: '))
if input_number == 1:
    hello_world()
elif input_number in (2, 3, 4):
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    if input_number == 2:
        print(f'Сумма чисел: {my_sum(x, y)}')
    elif input_number == 3:
        print(f'Первое число меньше второго? Ответ: {simple_compare(x, y)}')
    else:
        print(f'Результат сравнения: {compare(x, y)}')
elif input_number == 5:
    my_list = [int(number) for number in input('Введите числа, разделённые пробелов: ').split()]
    print(f'Мы удалили отрицательные числа из вашего списка: {filter_negative_numbers(my_list)}')
else:
    print('Задачи с таким номером нет.')