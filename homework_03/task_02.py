# Пользователь вводит число. Вывести True если чётное, иначе - False.

value = int(input('Введите число: '))
print(value % 2 == 0)  # или (not value % 2)
