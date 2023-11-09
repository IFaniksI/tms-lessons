# Импортируйте класс Person из первого задания
# from person import Person
# Создайте переменную my_friends - список из объектов класса Person.
# Добавьте в него некоторое количество вымышленных друзей с разными именами, возрастом и полом.
# Выведите информацию о каждом друге на экран.
# * Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# * Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter, либо генератор списков).
# * Заверните код из пунктов 5 и 6 в функции get_oldest_person и filter_male_person соответственно.

from person import Person

friends = [Person("Sergey", 15, "M"),
           Person("Wadim", 35, "M"),
           Person("Maria", 18, "F"),
           Person("Max", 25, "M"),
           Person("Masha", 29, "F")]

[i.print_person_info() for i in friends]


def get_oldest_person(friend):
    senior = friend[0]
    for i in friend:
        if i.age > senior.age:
            senior = i
    senior.print_person_info()


def filter_male_person(friend):
    [i.print_person_info() for i in friend if i.gender == 'M']
