# Запишите свои данные в файл file_06.csv в формате CSV.
# Пример:
# name,surname,gender
# Dmitry,Buevich,M

import csv

with open('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'surname', 'gender'])
    writer.writerow(['Dmitry', 'Buevich', 'M'])
