# Дано три числа. Вывести количество положительных чисел среди них.

x = int(input())
y = int(input())
z = int(input())
counter = 0

if x > 0:
    counter += 1
if y > 0:
    counter += 1
if z > 0:
    counter += 1

print(counter)
