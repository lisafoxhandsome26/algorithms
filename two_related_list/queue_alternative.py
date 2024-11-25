from queue import LifoQueue


class Queue:
    a = LifoQueue()
    b = LifoQueue()

    def push_back(self, x: int) -> None:
        self.a.put(x)

    def pop_front(self) -> int:
        if self.b.empty():
            while not self.a.empty():
                self.b.put(self.a.get())
        return self.b.get()
