# Дана строка. Посчитайте сколько раз в ней встречается символ "a".

my_str = 'qweasda'

count = 0
for value in my_str:
    if value == 'a':
        count += 1
print(count)
