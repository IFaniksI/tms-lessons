# Создайте класс MyTimeInterval, в котором два поля start и finish типа MyTime.
# Конструктор должен принимать start_seconds и finish_seconds.
# Добавьте метод is_inside, который принимает объект MyTime и возвращает True,
# если переданное время находится внутри интервала [start, finish]. Иначе False.
# * Добавьте метод intersects, который принимает
# другой объект MyTimeInterval и возвращает True если интервалы пересекаются. Иначе False.
# Протестируйте все методы с помощью assert.

from my_time import MyTime


class MyTimeInterval:
    def __init__(self, start_seconds: int, finish_seconds: int):
        self.start = MyTime(start_seconds)
        self.finish = MyTime(finish_seconds)

    def is_inside(self, time: MyTime) -> bool:
        return self.start <= time <= self.finish

    def intersects(self, other: 'MyTimeInterval') -> bool:
        # return self.start <= other.finish and self.finish >= other.start
        return (self.is_inside(other.start) or self.is_inside(other.finish) or
                other.is_inside(self.start) or other.is_inside(self.finish))


if __name__ == '__main__':
    interval = MyTimeInterval(10, 20)

    assert interval.is_inside(MyTime(15))
    assert interval.is_inside(MyTime(10))
    assert interval.is_inside(MyTime(20))
    assert not interval.is_inside(MyTime(5))
    assert not interval.is_inside(MyTime(25))

    assert interval.intersects(MyTimeInterval(5, 15))
    assert interval.intersects(MyTimeInterval(5, 25))
    assert interval.intersects(MyTimeInterval(10, 25))
    assert interval.intersects(MyTimeInterval(11, 19))
    assert not interval.intersects(MyTimeInterval(0, 5))
    assert not interval.intersects(MyTimeInterval(25, 30))
