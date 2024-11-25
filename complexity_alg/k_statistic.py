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


def kth_element(a: list[int], k: int) -> int:
    l = 0
    r = len(a)
    while l + 1 < r:
        m = partition(a, l, r)
        if k >= m:
            l = m
        else:
            r = m
    return a[l]


def median(a: list[int]) -> int:
    return kth_element(a, len(a) // 2)
