# * Дан словарь "слово" -> число. Вывести максимальное число среди значений словаря. Пример: {'a': 1, 'b': 2} -> 2.
# Примечание для 6 и 7 задания: чтобы пройти в цикле по всем элементам словаря можно использовать функцию items.
# my_dict = {'a': 1, 'b': 2}
# for key, value in my_dict.items():
#     print(key)
#     print(value)
# Данный код выведет в консоль
# a
# 1
# b
# 2

my_dict = {'a': 1, 'b': 2}

max_value = list(my_dict.values())[0]
for key, value in my_dict.items():
    if max_value <= value:
        max_value = value
print(max_value)

# print(max(my_dict.values()))
