# Напишите функцию my_sum, которая принимает два числа и возвращает их сумму.
# Проверьте корректность её работы при разных значениях аргументов. Например my_sum(1, 2), my_sum(25, 75) и т.д.

def my_sum(x: int | float, y: int | float) -> int | float:
    return x + y


assert my_sum(1, 2) == 3
assert my_sum(25, 75) == 100
