# Пользователь вводит свои данные (имя, фамилия, возраст). Запишите эти данные в файл file_07.csv формате CSV.

import csv

name = input('имя: ')
surname = input('фамилия: ')
age = input('возраст: ')

with open('file_07.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'surname', 'age'])
    writer.writerow([name, surname, age])
