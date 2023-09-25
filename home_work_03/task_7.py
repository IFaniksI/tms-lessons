# * Пользователь вводит число, выведите True если оно простое, иначе False.

value = int(input('Введите число: '))

variable = 2
while value % variable != 0:
    variable += 1

print(variable == value)

