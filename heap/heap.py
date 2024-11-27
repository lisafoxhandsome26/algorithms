class Heap:
    def __init__(self, a):
        self.a = [0]

    def size(self) -> int:
        return len(self.a) - 1

    def getMin(self) -> int:
        return self.a[0]

    def add(self, x: int) -> None:
        i = len(self.a)
        self.a.append(x)
        self.sift_up(i)

    def sift_up(self, i: int) -> None:
        if i == 0:
            return
        p = (i - 1) // 2
        if self.a[p] > self.a[i]:
            t = self.a[i]
            self.a[i] = self.a[p]
            self.a[p] = t
            self.sift_up(p)

    def pop(self) -> int:
        ret = self.getMin()
        self.a[0] = self.a[len(self.a) - 1]
        self.a.pop()
        self.sift_down(0)
        return ret

    def sift_down(self, i: int) -> None:
        if i * 2 + 1 >= len(self.a):
            return
        l = i * 2 + 1
        r = i * 2 + 2
        min_son = l
        if r < len(self.a) and self.a[r] < self.a[l]:
            min_son = r
        if self.a[min_son] >= self.a[i]:
            return
        t = self.a[i]
        self.a[i] = self.a[min_son]
        self.a[min_son] = t
        self.sift_down(min_son)


class Sorted:

    @staticmethod
    def sift_up(i: int, a: list, size: int) -> None:
        if i == 0:
            return
        p = (i - 1) // 2
        if a[p] > a[i]:
            t = a[i]
            a[i] = a[p]
            a[p] = t
            Sorted.sift_up(p, a, size)

    @staticmethod
    def sift_down(i: int, a: list, size: int) -> None:
        if i * 2 + 1 >= size:
            return
        l = i * 2 + 1
        r = i * 2 + 2
        min_son = l
        if r < size and a[r] < a[l]:
            min_son = r
        if a[min_son] >= a[i]:
            return
        t = a[i]
        a[i] = a[min_son]
        a[min_son] = t
        Sorted.sift_down(min_son, a, size)

    def sort(self, a: list) -> None:
        for i in range(0, len(a)):
            Sorted.sift_up(i, a, i + 1)

        size = len(a)
        for i in range(0, len(a)):
            size = len(a) - i
            t = a[0]
            a[0] = a[size - 1]
            a[size - 1] = t
            Sorted.sift_down(0, a, size - 1)


class MaxHeap:
    pass


class Main:
    def printMin2(self, a: list):
        m1 = a[0]
        m2 = a[1]
        if m1 > m2:
            t = m1
            m1 = m2
            m2 = t

        for i in range(2, len(a)):
            if a[i] > m2:
                continue
            if a[i] < m1:
                m2 = m1
                m1 = a[i]
            elif a[i] < m2:
                m2 = a[i]

    def printMinK(self, a: list, k: int):
        h = MaxHeap()
        for i in range(0, k):
            h.add(h, a[i])
        for i in range(k, len(a)):
            h.add(h, a[i])
            h.pop(h)
        for i in (0, k):
            print(h.pop(h))
