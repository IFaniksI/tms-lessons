# Запишите свои данные в файл file_09.xlsx в формате Excel.

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'Name'
sheet['A2'] = 'Dmitry'
sheet['B1'] = 'Surname'
sheet['B2'] = 'Buevich'
sheet['C1'] = 'Gender'
sheet['C2'] = 'M'

wb.save('file_09.xlsx')



