# Создайте класс Rational (рациональное число) с двумя приватными полями
# __numerator (числитель) и __denominator (знаменатель).
# Добавьте в класс методы-атрибуты (@property) numerator и denominator,
# которые возвращают __numerator и __denominator соответственно.
# Возможно у вас возникнет вопрос, зачем такие сложности, почему нельзя просто сделать поля публичными?
# Ответ: тогда их можно было бы изменить извне,
# а мы бы хотели чтобы извне можно было только читать их значения, но не записывать.
# Добавьте в класс магический метод __str__, который должен возвращать строку в формате "{nominator} / {denominator}".
# Теперь вы можете передавать объект Rational в функцию print и он будет напечатан так, как вы определили это.
# Переопределите магические методы умножения и деления.
# Они должны принимать второй объект типа Rational и возвращать новый объект того же типа.
# Для проверки можно использовать онлайн калькулятор дробей.
# * Переопределите магические методы сложения и вычитания.
# Не забудьте привести дроби к одинаковому знаменателю (шпаргалка).
# * Переопределите магические методы сравнения для операторов ==, !=, >=, <=, <, >.
# Возможно в процессе тестирования ваши дроби не сокращаются автоматически. Например в результате сложения
# Rational(1, 4) + Rational(1, 4) получится дробь 2 / 4, однако её можно сократить (нормализовать).
# * Напишите метод __normalise, который ничего не принимает (кроме self), и сокращает дробь.
# Для этого необходимо найти НОД (наибольший общий делитель) и разделить на него числитель и знаменатель.
# Вычислить НОД можно как максимальное число от 2 до min(nominator, denominator),
# на которые числитель и знаменатель делятся без остатка.
# Используйте метод __normalise в конструкторе. Убедитесь что код print(Rational(2, 4)) печатает на экран "1 / 2".
# Добавьте в метод __normalise нормализацию для знака
# (знаменатель всегда должен быть положительным, а знак дроби определяется знаком числителя).
# Например код print(Rational(-1, -2)) должен выводить на экран "1 / 2".
# Посчитайте значение выражения, используя только объекты класса Rational.

class Rational:
    def __init__(self, numerator: int, denominator: int):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalise()

    @property
    def numerator(self) -> int:
        return self.__numerator

    @property
    def denominator(self) -> int:
        return self.__denominator

    def __str__(self) -> str:
        return f'{self.__numerator} / {self.__denominator}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __sub__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__denominator - other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __eq__(self, other: 'Rational') -> bool:
        return self.__numerator * other.__denominator == other.__numerator * self.__denominator

    def __ne__(self, other: 'Rational') -> bool:
        return self.__numerator * other.__denominator != other.__numerator * self.__denominator

    def __ge__(self, other: 'Rational') -> bool:
        return self.__numerator * other.__denominator >= other.__numerator * self.__denominator

    def __le__(self, other: 'Rational') -> bool:
        return self.__numerator * other.__denominator <= other.__numerator * self.__denominator

    def __lt__(self, other: 'Rational') -> bool:
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __gt__(self, other: 'Rational') -> bool:
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    @staticmethod
    def nod(x: int, y: int) -> int:
        for i in range(min(abs(x), abs(y)), 0, -1):
            if x % i == 0 and y % i == 0:
                return i

    def __normalise(self):
        # gcd = math.gcd(self.numerator, self.denominator)
        nod = self.nod(self.__numerator, self.__denominator)
        self.__numerator //= nod
        self.__denominator //= nod

        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1


if __name__ == '__main__':
    assert Rational(2, 4) == Rational(1, 2)
    assert Rational(-1, -2) == Rational(1, 2)
    assert (Rational(1, 4) * (Rational(3, 2)
                              + Rational(1, 8))
            + Rational(156, 100) == Rational(1573, 800))

    assert str(Rational(1, 2)) == '1 / 2'
    assert Rational(1, 2) * Rational(2, 3) == Rational(1, 3)
    assert Rational(5, 15) / Rational(1, 3) == Rational(1, 1)
    assert Rational(1, 4) + Rational(1, 2) == Rational(3, 4)
    assert Rational(1, 2) - Rational(1, 4) == Rational(1, 4)
    assert Rational(9, 45) == Rational(1, 5)
    assert Rational(19, 56) != Rational(1, 45)
    assert Rational(2, 3) >= Rational(4, 6)
    assert Rational(4, 6) <= Rational(2, 3)
    assert Rational(2, 3) > Rational(2, 4)
    assert Rational(2, 4) < Rational(2, 3)


