# * Напишите функцию my_round, аналог встроенной round. Использование самой функции round запрещено.
# * Старайтесь использовать аннотации

def my_round(number, digits=0):
    multiplier = 10 ** digits
    if number < 0:
        return int(number * multiplier - 0.5) / multiplier
    else:
        return int(number * multiplier + 0.5) / multiplier


assert my_round(0.556) == 1.0
assert my_round(-10.4) == -10.0
assert my_round(-8.463, 2) == -8.46
assert my_round(18.658, 2) == 18.66

''' Можно и так
def my_round(number, digits=0):
    multiplier = 10 ** digits
    number *= multiplier
    if number - int(number) < 0.5:
        number = int(number)
    else:
        number = int(number) + 1
    return number / multiplier
'''