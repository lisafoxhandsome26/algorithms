class Heap:
    class Task:
        def __init__(self, ident, priority):
            self.ident = ident
            self.priority = priority

    def __init__(self):
        self.a = []
        self.pos = [0] * 1000

    def size(self) -> int:
        return len(self.a)

    def getMin(self) -> int:
        return self.a[0].ident

    def add(self, x):
        i = self.size()
        self.a.append(x)
        self.sift_up(i)

    def sift_up(self, i: int) -> None:
        if i == 0:
            return
        p = (i - 1) // 2
        if self.a[p].priority > self.a[i].priority:
            t = self.a[i]
            self.a[i] = self.a[p]
            self.a[p] = t

            self.pos[self.a[i].ident] = i
            self.pos[self.a[p].ident] = p

            self.sift_up(p)

    def pop(self) -> int:
        ret = self.getMin()
        self.a[0] = self.a[len(self.a) - 1]
        self.a.pop()
        self.pos[self.a[0].ident] = 0
        self.sift_down(0)
        return ret

    def sift_down(self, i: int) -> None:
        if i * 2 + 1 >= len(self.a):
            return
        l = i * 2 + 1
        r = i * 2 + 2
        min_son = l
        if r < len(self.a) and self.a[r].priority < self.a[l].priority:
            min_son = r
        if self.a[min_son].priority >= self.a[i].priority:
            return
        t = self.a[i]
        self.a[i] = self.a[min_son]
        self.a[min_son] = t

        self.pos[self.a[i].ident] = i
        self.pos[self.a[min_son].ident] = min_son

        self.sift_down(min_son)

    def push(self, t: Task):
        i = len(self.a)
        self.pos[t.ident] = i
        self.a.append(t)
        self.sift_up(i - 1)

    def set_priority(self, ident: int, priority: int) -> None:
        p = self.pos[ident]
        self.a[p].priority = priority
        self.sift_down(p)
        self.sift_up(p)
