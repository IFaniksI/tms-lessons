# Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.
# * Старайтесь использовать аннотации

import re


def get_longest_word(text: str) -> str:
    if re.match('^[a-zA-Z\s]*$', text):
        return max(text.split(), key=len)


assert get_longest_word('I saw Susie sitting in a shoeshine shop') == 'shoeshine'
assert get_longest_word('В Каннах львы только ленивым венки не вили') == None
assert get_longest_word('1 1234 12345 12 123') == None
assert get_longest_word('She sells seashells by the seashore') == 'seashells'
assert get_longest_word('Peter Piper picked a peck of pickled peppers.') == None
