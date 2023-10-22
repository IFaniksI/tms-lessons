# * Модернизируйте функцию из первой задачи дополнительными опциональными входными параметрами:
# · prompt - сообщение, которое увидит пользователь при введении данных. Значение по умолчанию - "" (пустая строка).
# · sep - разделитель, по которому разбивается строка. Значение по умолчанию - " " (пробел)
# · element_type - тип элементов (int, float или str), которые будут в возвращаемом списке. По умолчанию - int.


# с помощью обычного цикла
def input_list_with_simple_cycle(prompt="", sep=" ", element_type: type = int) -> list:
    input_strings = input(prompt).split(sep)
    output_numbers = []
    for element in input_strings:
        output_numbers.append(element_type(element))
    return output_numbers


# с помощью генератора списков
def input_list_with_generator(prompt="", sep=" ", element_type: type = int) -> list:
    return [element_type(element) for element in input(prompt).split(sep)]


# с помощью функции map
def input_list_with_map(prompt="", sep=" ", element_type: type = int) -> list:
    return list(map(element_type, input(prompt).split(sep)))


print(input_list_with_simple_cycle('Введите числа с плавающей точкой через запятую: ', ',', float))
print(input_list_with_generator('Введите числа с плавающей точкой через запятую: ', ',', float))
print(input_list_with_map('Введите числа с плавающей точкой через запятую: ', ',', float))