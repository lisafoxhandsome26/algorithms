def merge(a: list[int], b: list[int]) -> list[int]:
    res = []
    pt1, pt2 = 0, 0
    while pt1 < len(a) or pt2 < len(b):
        if pt1 == len(a):
            res.append(b[pt2])
            pt2 += 1
            continue
        if pt2 == len(b):
            res.append(a[pt1])
            pt1 += 1
            continue
        if a[pt1] < b[pt2]:
            res.append(a[pt1])
            pt1 += 1
        else:
            res.append(b[pt2])
            pt2 += 1
    return res


# a1 = [1, 2, 5, 3, 7]
# a2 = [2, 4, 6, 7, 8]
# result = merge(a1, a2)
# print(result)


def sorted_m(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
    m = len(a) // 2
    return merge(
        sorted_m(a[:m]),
        sorted_m(a[m:])
    )

g = [5, 2, 3, 45, 12, 8, 55, 1]

f = sorted_m(g)
print(f)
