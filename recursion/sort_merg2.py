def merge(a: list[int], buf: list[int], l, m, r) -> None:
    pt1, pt2, rp = l, m, 0
    while pt1 < m or pt2 < r:
        if pt1 == m:
            buf[rp] = a[pt2]
            pt2 += 1
            rp += 1
            continue
        if pt2 == r:
            buf[rp] = a[pt1]
            pt1 += 1
            rp += 1
            continue
        if a[pt1] < a[pt2]:
            buf[rp] = a[pt1]
            pt1 += 1
            rp += 1
        else:
            buf[rp] = a[pt2]
            pt2 += 1
            rp += 1
    for i in range(l, r):
        a[i] = buf[i - l]


def sorted_m(a: list[int], l, r: int, buf: list[int]) -> None:
    if r - l <= 1:
        return
    m = (r + l) // 2

    sorted_m(a, l, m, buf)
    sorted_m(a, m, r, buf)
    merge(a, buf, l, m, r)


def sort_m(a: list[int]) -> None:
    buf = [0] * len(a)
    sorted_m(a, 0, len(a), buf)


g = [5, 2, 3, 45, 12, 8, 55, 1]
sort_m(g)
print(g)
