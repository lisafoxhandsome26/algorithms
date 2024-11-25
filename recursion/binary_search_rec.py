# Итеративный бинарный поиск
def lower_bound(a: list[int], key: int) -> str:
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] < key:
            l = m + 1
        elif a[m] > key:
            r = m - 1
        else:
            return f"Element {key} was found."
    return f"Element {key} das not exists."


# Рекурсивный бинарный поиск
def lower_bound_rec(a: list[int], key: int, l: int, r: int) -> int:
    if l + 1 >= r:
        return r
    m = (l + r) // 2
    if a[m] >= key:
        return lower_bound_rec(a, key, l, m)
    else:
        return lower_bound_rec(a, key, m, r)


def run_lower_bound_rec(a: list[int], key: int) -> int:
    return lower_bound_rec(a, key, -1, len(a))


f = list(range(50))
res = lower_bound(f, 1555)
print(res)
