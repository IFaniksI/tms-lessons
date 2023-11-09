# Создайте класс Animal, У класса должно быть два поля: name, age.
# Все поля должны заполняться в конструкторе класса (метод __init__).
# Создайте класс Dog, наследующийся от класса Animal. Помимо полей name и age от базового класса,
# в классе должно быть поле breed (порода). Все три поля должны заполняться в конструкторе.
# Используйте super().__init__(name, age) для вызова конструктора Animal.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


# создание объекта
my_dog = Dog('Шарик', 10, 'Доберман')

# вывод поля класса Dog
print(my_dog.breed)

# вывод полей класса, унаследованных от класса Animal
print(my_dog.name)
print(my_dog.age)

'''
Ожидаемый вывод:
Доберман
Шарик
10
'''
