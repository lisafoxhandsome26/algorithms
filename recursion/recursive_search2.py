s = [0] * 3


# Если в примере нет двух повторяющих ся букв подряд
def gen(c, n: int) -> None:
    if c == n:
        for i in range(1, n):
            if s[i] == s[i - 1]:
                return
        print(s)
        return
    for s[c] in ['a', 'b', 'c', 'd', 'e', 'f']:
        gen(c + 1, n)


def gen2(x, n: int) -> None:
    if x == n:
        print(s)
        return
    for s[x] in ['a', 'b', 'c', 'd', 'e', 'f']:
        if x > 0:
            if s[x] == s[x - 1]:
                continue
        gen(x+1, n)


#print(gen2(0, 3))


# Битовая маска, которая умеет хранить массив из 0 и 1, используя на каждый индекс 1 бит памяти
class Bitset:
    def __init__(self, n: int) -> None:
        self.data = [0] * (n // 32 + 1)

    def get(self, ind: int) -> int:
        x = self.data[ind // 32]
        return (x >> (ind % 32)) & 1

    def set(self, ind, val: int) -> None:
        if self.get(ind) == val:
            return
        self.data[ind // 32] ^= 1 << (ind % 32)


a = Bitset(1)


def gen3(x, n, k: int) -> None:
    if k < 0:
        return
    if k > (n - x):
        return
    if x == n:
        for i in range(0, n):
            print(a.get(i))
        print("")
        return
    a.set(x, 0)
    gen3(x+1, n, k)
    s.set(x, 1)
    gen3(x+1, n, k-1)


gen3(0, 3, 2)
