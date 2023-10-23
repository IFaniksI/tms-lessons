# Дан список чисел. Найти их максимальное среди них.

my_list = [4, 1, 5, 2, 3]

maxx = my_list[0]
for value in my_list:
    if maxx <= value:
        maxx = value
print(maxx)

# print(max(int(value) for value in input().split()))
