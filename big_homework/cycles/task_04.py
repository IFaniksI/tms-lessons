# Дан список чисел. Если среди них есть ноль - вывести yes, иначе no.

my_list = [1, 2, 0, 4, 5]

for value in my_list:
    if value == 0:
        print('yes')
        break
else:
    print('no')

# print('yes') if 0 in my_list else print('no')
