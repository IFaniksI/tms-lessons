# Пользователь вводит число. Посчитайте сумму цифр этого числа.
# Количество цифр числа может быть произвольными
# Примеры:
# 12345 -> 1 + 2 + 3 + 4 + 5 = 15
# 15 -> 1 + 5 = 6

value = input('Введите число: ')
result = 0
for i in value:
    result += int(i)
print(result)
