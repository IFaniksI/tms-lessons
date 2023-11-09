# Пользователь вводит свои данные (имя, фамилия, возраст). Запишите эти данные в файл file_04.json формате JSON.

import json

name = input('имя: ')
surname = input('фамилия: ')
age = input('возраст: ')

deta = {'name': name, 'surname': surname, 'age': age}

with open('file_04.json', 'w') as file:
    json.dump(deta, file)
