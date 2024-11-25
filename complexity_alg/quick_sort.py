import random


def partition(a: list[int], l, r: int) -> int:
    if r - l < 1:
        return l
    i = l
    j = r - 1
    x = a[l + random.randint(0, (r - l))]
    while i < j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i += 1
            j -= 1
        else:
            break
    return i


def qsort(a: list[int], l, r: int) -> None:
    if r - l <= 1:
        return
    m = partition(a, l, r)
    if m - l > r - m:
        qsort(a, m, r)
        r = m
    else:
        qsort(a, l, m)
        l = m
