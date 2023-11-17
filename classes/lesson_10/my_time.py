# Создайте класс MyTime с одним полем seconds (типа float).
# Добавьте методы-свойства (@property) hours и minutes,
# которые возвращают int (целое количество часов и минут соответственно).
# Переопределите магические методы умножения и деления на число. Пример: MyTime(5) * 2 будет равно MyTime(10).
# Переопределите магические методы сложения и вычитания с другим объектом MyTime.
# Пример: MyTime(5) + MyTime(2) будет равно MyTime(7).
# * Добавьте метод get_formatted_str, который возвращает строку в формате "HH:MM:SS.S".
# Например для MyTime(3724.5) этот метод должен возвращать строку "01:02:04.5".
# Проверьте что выводит print(MyTime(10))
# Добавьте магический метод __str__, который возвращает строку в формате "{seconds}s" (количество секунд + суффикс s).
# Переопределите магические методы сравнения (==, !=, >=, <=, <, >).
# В блоке if __name__ == '__main__' напишите тесты для ВСЕХ методов и операторов класса MyTime.
# Для проверки используйте ключевое слово assert.

class MyTime:
    def __init__(self, seconds: float):
        self.seconds = seconds

    @property
    def hours(self) -> int:
        return int(self.seconds // 3600)

    @property
    def minutes(self) -> int:
        return int(self.seconds // 60 % 60)

    def __mul__(self, number: int | float) -> 'MyTime':
        return MyTime(self.seconds * number)

    def __truediv__(self, number: int | float) -> 'MyTime':
        return MyTime(self.seconds / number)

    def __add__(self, other: 'MyTime') -> 'MyTime':
        return MyTime(self.seconds + other.seconds)

    def __sub__(self, other: 'MyTime') -> 'MyTime':
        return MyTime(self.seconds - other.seconds)

    def get_formatted_str(self) -> str:
        return f'{self.hours:02d}:{self.minutes:02}:{self.seconds % 60:04.1f}'

    def __str__(self) -> str:
        return f'{self.seconds}s'

    def __lt__(self, other: 'MyTime') -> bool:
        return self.seconds < other.seconds

    def __le__(self, other: 'MyTime') -> bool:
        return self.seconds <= other.seconds

    def __eq__(self, other: 'MyTime') -> bool:
        return self.seconds == other.seconds

    def __ne__(self, other: 'MyTime') -> bool:
        return self.seconds != other.seconds

    def __gt__(self, other: 'MyTime') -> bool:
        return self.seconds > other.seconds

    def __ge__(self, other: 'MyTime') -> bool:
        return self.seconds >= other.seconds


if __name__ == '__main__':
    time = MyTime(3724.5)
    assert time.hours == 1
    assert time.minutes == 2
    assert MyTime(10) * 2 == MyTime(20)
    assert MyTime(10) / 2 == MyTime(5)
    assert MyTime(2) + MyTime(2) == MyTime(4)
    assert MyTime(5) - MyTime(2) == MyTime(3)
    assert time.get_formatted_str() == '01:02:04.5'
    assert str(time) == '3724.5s'
    assert MyTime(10) < MyTime(11)
    assert MyTime(10) <= MyTime(11)
    assert MyTime(10) <= MyTime(10)
    assert MyTime(5) == MyTime(5)
    assert MyTime(5) != MyTime(3)
    assert MyTime(5) > MyTime(3)
    assert MyTime(5) >= MyTime(3)
    assert MyTime(5) >= MyTime(5)
