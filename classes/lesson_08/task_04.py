# Создайте класс User с публичным поле login и приватным полем __password. Оба поля должны заполняться в конструкторе.
# Добавьте метод check_password, который принимает строку с паролем (возможно неправильным), и возвращает
# True, если пароль верный
# False, если пароль неверный
# Добавьте метод reset_password, который принимает строку с новым паролем и обновляет поле __password новым значением.

class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def reset_password(self, new_password):
        self.__password = new_password


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
