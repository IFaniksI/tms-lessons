# Пользователь вводит свои данные (имя, фамилия, возраст). Запишите эти данные в файл file_10.xlsx формате Excel.

import openpyxl

name = input('имя: ')
surname = input('фамилия: ')
age = input('возраст: ')

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Age'

sheet['A2'] = name
sheet['B2'] = surname
sheet['C2'] = age

wb.save('file_10.xlsx')
