def input_int_number() -> int:
    while True:
        try:
            return int(input('Введите целое число: '))
        except ValueError as e:
            print('Ошибка: ', e)
            print('Попробуйте снова.')


class CalculationExitException(Exception):
    pass


def calculate(left: int, right: int, operation: str) -> float | int:
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right
    elif operation == '!':
        raise CalculationExitException()
    else:
        raise ValueError(f'Неподдерживаемая операция: {operation}')


def main():
    while True:
        try:
            left = input_int_number()
            right = input_int_number()
            operation = input('Введите операцию (введите ! для выхода из программы): ')
            result = calculate(left, right, operation)
            print('Результат операции:', result, end='\n\n')
        except ValueError or ZeroDivisionError as e:  # или так (ValueError, ZeroDivisionError)
            print('Ошибка:', e, end='\n\n')
        except CalculationExitException:
            print('Завершаем программу')
            break


if __name__ == '__main__':
    main()

# Всё задание будет в файле calculator.py.
# Наша задача: сделать приложение "Калькулятор",
# которое будет запрашивать у пользователя два целых числа и операцию (+, -, *, /) и выполняет эту операцию.
# Для завершения программы необходимо будет ввести операцию ! (восклицательный знак).
# Программа должна будет обработать все возможные ошибки, такие как неправильный ввод пользователя.
# В комментарии к слайду пример работы программы.
# Создайте функцию input_int_number, которая ничего не принимает и возвращает int.
# Функция должна печатать "Введите целое число:" до тех пор, пока пользователь не введёт корректное число.
# Пока пользователь вводит некорректное число - выводите сообщение об ошибке и попросите ввести число снова.
# Используйте while True, try, except.
# Создайте функцию calculate, которая принимает два целых числа (left и right), и операцию (строку).
# Если строка operation одна их поддерживаемых операций (+, -, *, /) выполните эту операцию.
# Иначе - выбросьте исключение ValueError(f'Неподдерживаемая операция: {operation}')
# Создайте функцию main. Это будет главной функцией вашей программы.
# Функция должна запускать бесконечный цикл, запрашивать у пользователя два числа и операцию,
# и выводить результат операции (передавая введённые данные в функцию calculate).
# Внутри цикла вам необходимо добавить блок try-except для обработки исключений ValueError (вспомните прошлое задание)
# и ZeroDivisionError. В случае исключения нужно вывести сообщение об ошибке и продолжить работу.
# Добавьте блок if __name__ == '__main__', в котором будет вызов функции main.
# До сих пор мы не продумали каким образом будет осуществляться выход из программы.
# В этом задании предлагается использовать собственный тип исключения для этого.
# Создайте класс CalculationExitException, наследуемый от Exception.
# Внутри функции calculate выбросьте (raise) созданное исключение в случае,
# если переданная операция это ! (восклицательный знак).
# Обработайте это исключение внутри функции main в дополнительном блоке except.
# Выведите сообщение "Завершаем программу" и выйдите из бесконечного цикла.
# В функции main есть код справа.
# Обратите внимание, что два первых блока идентичны. Объедините их в один с помощью их общего класса-предка Exception.
# Удостоверьтесь, что программа всё ещё работает правильно и завершается корректно.