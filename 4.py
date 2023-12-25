def reverse_string(string: str) -> str:
    return string[::-1]


def is_string_palindrome(string: str) -> bool:
    return string.lower().replace(' ','') == string[::-1].lower().replace(' ', '')


some_string = 'Папа мыл раму'
some_palindromes = ['Аргентина манит негра',
                   'Коту скоро сорок суток',
                   'Уверен и не реву']