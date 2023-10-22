# Вам даны реализации базовых математических операций с целыми числами.
# Вопрос: что будет, если передать в эти функции что-то другое вместо чисел. Например вызвать minus('hello', [123]).
# Ваша задача сделать так, чтобы при вызове каждой функции проводилась проверка типов переменных x и y
# c помощью выражения isinstance(x, int). В случае, если одна из переменных НЕ является целым числом - печатаем
# сообщение об ошибке "Expected int type" в консоль и возвращали None.
# Для простоты можно сначала изменить код одной из функций так, чтобы она сама делала эти проверки.
# Конечная цель - выполнить требования задачи НЕ меняя код самих функций, а создать функцию-декоратор check_types,
# пометив каждую из функций вашим декоратором (@check_types)


def check_types(original_func):
    def update_func(x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            print("Expected int type")
            return None
        return original_func(x, y)
    return update_func


@check_types
def plus(x, y):
    return x + y

@check_types
def minus(x, y):
    return x - y

@check_types
def mult(x, y):
    return x * y

@check_types
def div(x, y):
    return x / y


print(plus(1, 2))
print(minus('1', 2))
print(mult(5, 2.0))
print(div([], {}))