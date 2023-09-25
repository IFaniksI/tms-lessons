# Пользователь вводит два числа: x, y, где x - сумма рублей,
# которую он кладёт на депозит под 10% годовых, y - количество лет.
# Каждый год вклад увеличивает на 10%. Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты
# Вывести конечную сумму на счету по прошествии y лет.
# Пример: x = 100, y = 2
# Решение: 100 + 10% = 110 (первый год) => 110 + 10% = 121 (второй год)
# Ответ: 121
# Подсказка: для решения задачи не обязательно использовать циклы. Достаточно будет возведения в степень.

x = int(input('Введите сумму рублей: '))
y = int(input('Введите количество лет: '))

print(int(x * 1.1 ** y))