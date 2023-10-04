# Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный, False если нет.
# Распределение високосных годов:
# · год, номер которого кратен 400, — високосный;
# · остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
# · остальные годы, номер которых кратен 4, — високосные;
# · все остальные годы — невисокосные.

def is_year_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


assert is_year_leap(2020) == True
assert is_year_leap(2022) == False
assert is_year_leap(2024) == True
assert is_year_leap(1600) == True
assert is_year_leap(2000) == True
assert is_year_leap(1700) == False
assert is_year_leap(2300) == False

