def sort(a: list[int]) -> None:
    c = [0] * 3650
    for i in range(0, 3650):
        c[i] = [0]
    for i in range(0, len(a)):
        c[a[i]].append(a[i])
    pt = 0
    for i in range(0, 3650):
        for j in range(1, len(c[i])):
            a[pt] = c[i].pop()
            pt += 1


def sort2(a: list[int]) -> None:
    cnt = [0] * 3650
    for i in range(0, len(a)):
        cnt[a[i]] += 1
    for i in range(1, 3650):
        cnt[i] = cnt[i] + cnt[i-1]

    for i in range(3650-1, 0, -1):
        cnt[i] = cnt[i-1]
    cnt[0] = 0
    b = [0] * len(a)
    for i in range(0, len(a)):
        b[cnt[a[i]]] = a[i]
        cnt[a[i]] += 1
    for i in range(0, len(a)):
        a[i] = b[i]

f = [5, 3, 7, 23, 4, 5, 1, 56, 22, 45, 66, 66]
sort(f)
print(f)
