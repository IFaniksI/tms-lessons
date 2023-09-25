# Форматирование времени
# Пользователь вводит в консоли число секунд.
# Выведите число секунд в виде:
# 1. минуты:секунды.
# 2. *дни:часы:минуты:секунды.

value = int(input("Введите число секунд: "))
minutes = value // 60
seconds = value % 60
print(f'{minutes}:{seconds}')  # 1
minutes = value % 60
hour = value // 3600
print(f'{hour}:{minutes}:{seconds}')  # 2
