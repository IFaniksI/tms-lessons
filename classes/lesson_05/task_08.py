# * Напишите функцию my_round, аналог встроенной round. Использование самой функции round запрещено.
# * Старайтесь использовать аннотации

def my_round(number: float, digits: int = 0) -> float:
    multiplier = 10 ** digits
    if number < 0:
        return int(number * multiplier - 0.5) / multiplier
    else:
        return int(number * multiplier + 0.5) / multiplier


assert my_round(0.556) == 1.0
assert my_round(-10.4) == -10.0
assert my_round(-8.463, 2) == -8.46
assert my_round(18.658, 2) == 18.66

''' более понятный вариант
def my_round(num: float, digits: int = 0) -> float:
    ten_pow = 10 ** digits
    num *= ten_pow
    if num - int(num) < 0.5:
        num = int(num)
    else:
        num = int(num) + 1
    num /= ten_pow
    return num
'''
