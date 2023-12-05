# Напишите программу на Python, которая подключается к вашей базе данных и выводит на экран всех людей.
# Затем программа спрашивает у пользователя минимальный возраст и выводит на экран людей,
# не младше введённого количества лет в порядке возрастания возраста.

import sqlite3


with sqlite3.connect('sqlite.db') as connection:
    all_users = connection.execute('SELECT * FROM user;')
    for user in all_users.fetchall():
        print(user)

    min_age = int(input('минимальный возраст: '))
    users = connection.execute('SELECT * FROM user WHERE age >= ? ORDER BY age;', (min_age,))
    for user in users.fetchall():
        print(user)
