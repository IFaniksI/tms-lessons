# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать до тех пор,
# пока ответ не будет корректным.

for i in range(0, 101):
    print(i, '\nShould we break? ')
    answer = input()
    while answer != 'no' and answer != 'yes':
        answer = input('Dont understand you ')
    if answer == 'yes':
        break
