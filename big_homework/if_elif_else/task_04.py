# Дано число. Если оно положительно - выведите positive, если отрицательно - negative, если равно нулю - zero.

x = int(input())

if x > 0:
    print('positive')
elif x < 0:
    print('negative')
else:
    print('zero')

# print('positive' if x > 0 else 'negative' if x < 0 else 'zero')
