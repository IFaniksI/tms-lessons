# Напишите программу "Телефонная книга", в которой пользователь сможет сохранять контакты
# (уникальное имя и номер телефона) в которой пользователю в бесконечном цикле будет предлагаться
# список поддерживаемых операций:
# 0. Выйти из программы
# 1. Добавить новый контакт
# 2. Вывести весь список контактов в алфавитном порядке.
# 3. Обновить номер контакта
# Все операции должны делаться через запросы в базу данных (SELECT, INSERT, UPDATE).
# Название таблицы и столбцов в базе продумайте сами.

import sqlite3


def add_contact(name: str, phone_number: str):
    with sqlite3.connect(DB_FILE) as connection:
        connection.execute('INSERT INTO contact VALUES(?, ?)', (name, phone_number))


def print_all_contacts():
    with sqlite3.connect(DB_FILE) as connection:
        all_contact = connection.execute('SELECT * FROM contact')
        for name, phone_number in all_contact.fetchall():
            print(name, phone_number)


def update_contact(name: str, new_phone_number: str):
    with sqlite3.connect(DB_FILE) as connection:
        connection.execute('UPDATE contact SET phone_number = ? WHERE name = ?', (new_phone_number, name))


def main():
    while True:
        print('Выберите действие:\n'
              '0. Выйти из программы\n'
              '1. Добавить новый контакт\n'
              '2. Вывести весь список контактов в алфавитном порядке.\n'
              '3. Обновить номер контакта\n')

        operation = input()
        if operation == '0':
            break
        elif operation == '1':
            name = input('Имя контакта: ')
            phone_number = input('Номер контакта: ')
            add_contact(name, phone_number)
        elif operation == '2':
            print_all_contacts()
        elif operation == '3':
            name = input('Имя существующего контакта: ')
            new_phone_number = input('Новый номер контакта: ')
            update_contact(name, new_phone_number)
        else:
            print('Не поддерживаемая операция!')


if __name__ == '__main__':
    DB_FILE = 'phone_book.db'
    main()
