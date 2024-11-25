import string


def search_password1():
    for s1 in string.ascii_uppercase:
        for s2 in string.ascii_uppercase:
            for s3 in string.ascii_uppercase:
                for s4 in string.ascii_uppercase:
                    print(s1, s2, s3, s4)


def search_password2():
    possible = []
    for i in 'abcdefghijklmnopqrstuvwxyz':
        possible.append(i)
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        possible.append(i)
    for i in '0123456789':
        possible.append(i)
    for s1 in possible:
        for s2 in possible:
            for s3 in possible:
                for s4 in possible:
                    print(s1, s2, s3, s4)


# Рекурсивный перебор всех паролей длины n, начиная с позиции символа x
s = [0] * 3


def gen(c, n: int) -> None:
    if c == n:
        print(s)
        return
    for s[c] in ['a', 'b', 'c', 'd', 'e', 'f']:
        gen(c + 1, n)

gen(0, 3)
