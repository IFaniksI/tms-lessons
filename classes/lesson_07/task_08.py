# Прочитайте файл из прошлого задания и выведите данные в формате "{Фамилия} {Имя} {Возраст}".

import csv

with open('file_07.csv') as file:
    reader = csv.reader(file, delimiter=',')
    header = False
    for row in reader:
        if not header:
            header = True
            continue
        print(row[1], row[0], row[2])
