# Дан номер месяца (число от 1 до 12). Выведите пору года, которой этот месяц принадлежит: зима, весна, лето или осень.

x = int(input())

if x <= 2 or x == 12:
    print('зима')
elif 3 <= x <= 5:
    print('весна')
elif 6 <= x <= 8:
    print('лето')
else:
    print('осень')

# print('зима' if x <= 2 or x == 12 else 'весна' if 3 <= x <= 5 else 'лето' if 6 <= x <= 8 else 'осень')