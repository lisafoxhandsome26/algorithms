import io
import random
import time


def exp1():
    s = set()
    for i in range(0, 10_000_000):
        s.add(i)

    start_time = time.time()
    cnt = 0
    for i in range(0, 10_000_000):
        if i not in s:
            cnt += 1

    print("--- %s seconds ---" % round(time.time() - start_time, 4))


def exp2():
    n = 10_000_000
    a = [0] * n
    for i in range(0, n):
        a[i] = random.randint(0, 800_000)

    a.sort()
    start_time = time.time()
    cnt = 0
    for i in range(0, 10_000_000):
        if a[i] < n // 2:
            cnt += 1

    print("--- %s seconds ---" % round(time.time() - start_time, 4))


def exp3():
    n = 10_000_000
    f = io.BytesIO()
    start_time = time.time()
    for i in range(0, n):
        f.write("c".encode('utf-8'))
    f.close()

    print("--- %s seconds ---" % round(time.time() - start_time, 4))
