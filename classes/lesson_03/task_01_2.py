# Форматирование времени
# Пользователь вводит в консоли число секунд.
# Выведите число секунд в виде:
# 2. *дни:часы:минуты:секунды.

value = int(input("Введите число секунд: "))
days = value // 86400
hours = value % 86400 // 3600
minutes = value % 3600 // 60
seconds = value % 60
print(f'{days}:{hours}:{minutes}:{seconds}')