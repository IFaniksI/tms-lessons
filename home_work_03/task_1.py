# Пользователь вводит одно число, сторона квардата.
# Вывести кортеж из трёх чисел: периметр квадрата, площадь квадрата, диагональ квадрата.

side = int(input('Введите число, сторона квардата: '))

perimeter = side * 4
square = side ** 2
diagonal = side * 2 ** 0.5

print((perimeter, square, diagonal))
