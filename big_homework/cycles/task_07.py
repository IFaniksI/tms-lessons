# * Дан словарь "слово" -> число. Вывести ключ, соответствующий максимальному значению.
# Пример: {'a': 1, 'b': 2} -> 'b'.

my_dict = {'a': 1, 'b': 2}


max_value = list(my_dict.values())[0]
max_key = list(my_dict.keys())[0]

for key, value in my_dict.items():
    if max_value <= value:
        max_value = value
        max_key = key
print(max_key)

