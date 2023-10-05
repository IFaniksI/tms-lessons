# Напишите функцию list_sum, которая принимает на вход список и возвращает сумму элементов списка.
# Использование встроенной функции sum запрещено.
# * Старайтесь использовать аннотации

def list_sum(value: list[int]) -> int:
    a: int = 0
    for i in value:
        a += i
    return a


assert list_sum([1, 2, 3]) == 6
assert list_sum([-1, 2, -3]) == -2
