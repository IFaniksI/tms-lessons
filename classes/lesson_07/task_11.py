# Прочитайте файл из прошлого задания и выведите данные в формате "{Фамилия} {Имя} {Возраст}".

import openpyxl

wb = openpyxl.load_workbook('file_10.xlsx')
sheet = wb.active
print(sheet['B2'].value, sheet['A2'].value, sheet['C2'].value)

