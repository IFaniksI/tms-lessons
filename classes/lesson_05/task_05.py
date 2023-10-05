# Напишите функцию is_palindrome, которая принимает на вход строку, и возвращает True если это палиндром, иначе False.
# * Старайтесь использовать аннотации

def is_palindrome(string: str) -> bool:
    return string == string[::-1]


assert is_palindrome('opo') == True
assert is_palindrome('pio') == False
assert is_palindrome('ggg') == True
