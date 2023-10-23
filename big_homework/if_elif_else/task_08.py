# * Даны три числа, выведите максимальное из них
# (не используя функцию max и не создавая дополнительных переменных
# и сделав не более 2 сравнений для нахождения результата).

x = int(input())
y = int(input())
z = int(input())

if x >= y:
    if x >= z:
        print(x)
    else:
        print(z)
else:
    if y >= z:
        print(y)
    else:
        print(z)
