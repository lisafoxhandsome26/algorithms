import random


class Segment:
    def __init__(self, l, r):
        self.l = l
        self.r = r


def solve(segments: list[Segment]) -> int:
    if not segments:
        return 0
    segments.sort(key=lambda x: x.r)
    last_r = segments[0].l
    ans = 0
    for i in segments:
        if i.l >= last_r:
            ans += 1
            last_r = i.r
    return ans


def solve_slow(segments: list[Segment]) -> int:
    ans = 0
    for mask in range(0, 1 << len(segments)):
        intersect = False
        for i in range(0, len(segments)):
            for j in range(i+1, len(segments)):
                if mask & (1 << i) == 0:
                    continue
                if mask & (1 << j) == 0:
                    continue
                l = max(segments[i].l, segments[j].l)
                r = min(segments[i].r, segments[j].r)
                if l < r:
                    intersect = True
                    break
        if not intersect:
            cnt = 0
            for i in range(0, len(segments)):
                if (mask & (1 << i)) > 0:
                    cnt += 1
            if cnt > ans:
                ans = cnt
    return ans


def gen() -> list[Segment]:
    test = []
    N = random.randint(1, 10)
    for i in range(0, N):
        r = random.randint(1, 100)
        l = random.randint(r, 101)
        test.append(Segment(l, r))
    return test


def stress_test() -> None:
    for n in range(1, 11):
        test = gen()
        if solve_slow(test) != solve(test):
            print("Stress failed")
            print(len(test))
            for i in range(0, len(test)):
                print(test[i].l + " " + test[i].r)
                print(" ")
        else:
            print(f"Stress test {n} passed")


stress_test()
