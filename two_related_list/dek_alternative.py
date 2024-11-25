from queue import LifoQueue


class Deque:
    a = LifoQueue()
    b = LifoQueue()

    def push_back(self, x: int) -> None:
        self.a.put(x)

    def push_front(self, x: int) -> None:
        self.b.put(x)

    def rebalance(self) -> None:
        t = LifoQueue()
        s1 = self.a
        s2 = self.b
        if self.a.empty():
            s1 = self.b
            s2 = self.a
        d = s1.qsize() // 2
        for i in range(0, d):
            t.put(s1.get())
        while not s1.empty():
            s2.put(s1.get())
        while not t.empty():
            s1.put(t.get())

    def pop_back(self) -> int:
        if self.a.empty():
            self.rebalance()
        return self.a.get()

    def pop_front(self) -> int:
        if self.b.empty():
            self.rebalance()
        return self.b.get()
