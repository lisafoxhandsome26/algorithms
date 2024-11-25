def sort(a: list[int]) -> None:
    cnt = [0] * 1000
    for i in range(0, len(a)):
        cnt[a[i]] += 1
    pt = 0
    for i in range(0, len(cnt)):
        for j in range(0, cnt[i]):
            a[pt] = i
            pt += 1
