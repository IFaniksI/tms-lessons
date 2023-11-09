# Скопируйте класс из предыдущего задания.
# Давайте теперь хранить пароль в зашифрованном виде. Создайте новое поле __key = random.randint(1, 1000)
# Добавьте приватный метод __encode, шифрующий строку:
# def __encode(self, s):
#     return ''.join([chr(ord(i) ^ self.__key) for i in s])
# Используйте метод __encode:
# В конструкторе, при инициализации поля __password
# В методе check_password
# В методе reset_password
# Перепишите код из комментария к ПРЕДЫДУЩЕМУ СЛАЙДУ, удостоверьтесь что результат такой же.
# В этом и есть сила инкапсуляции, мы можем как угодно менять внутреннюю реализацию нашего класса,
# при этом не нужно менять код, который использовал наш класс.

import random


class User:
    def __init__(self, login, password):
        self.login = login
        self.__key = random.randint(1, 1000)
        self.__password = self.__encode(password)

    def check_password(self, password):
        return self.__password == self.__encode(password)

    def reset_password(self, new_password):
        self.__password = self.__encode(new_password)

    def __encode(self, s):
        return ''.join([chr(ord(i) ^ self.__key) for i in s])


my_user = User('dima_buevich', 'SuperSecretP@ssword')

print(my_user.login)
# print(my_user.__password)  # так нельзя, будет ошибка

print(my_user.check_password('WrongPassword'))
print(my_user.check_password('SuperSecretP@ssword'))

my_user.reset_password('NewP@ssword')

print(my_user.check_password('SuperSecretP@ssword'))
print(my_user.check_password('NewP@ssword'))

'''
Ожидаемый результат:
dima_buevich
False
True
False
True
'''