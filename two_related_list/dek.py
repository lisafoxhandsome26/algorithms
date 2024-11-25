class Deque:
    def __init__(self, max_size: int) -> None:
        self.head = 0
        self.tail = 0
        self.data = [None] * max_size

    def empty(self) -> bool:
        if self.head == self.tail:
            return True
        return False

    def double_size(self) -> None:
        d = [None] * len(self.data) * 2
        pt = 0
        if self.head <= self.tail:
            for i in range(self.head, self.tail):
                d[pt] = self.data[i]
                pt += 1
        else:
            for i in range(self.head, len(self.data)):
                d[pt] = self.data[i]
                pt += 1
            for i in range(0, self.tail):
                d[pt] = self.data[i]
                pt += 1

        self.data = d
        self.head = 0
        self.tail = pt

    def push_back(self, x: int) -> None:
        if (
                (self.tail + 1 == self.head) or
                ((self.tail + 1 == len(self.data) and (self.head == 0)))
        ):
            self.double_size()
        self.data[self.tail] = x
        self.tail += 1
        if self.tail >= len(self.data):
            self.tail = 0

    def push_front(self, x: int) -> None:
        prev = self.head - 1
        if prev < 0:
            prev = len(self.data) - 1
        if prev == self.tail:
            self.double_size()
            prev = len(self.data) - 1

        self.data[prev] = x
        self.head = prev

    def pop_front(self) -> int:
        t = self.data[self.head]
        self.data[self.head] = 0
        self.head += 1
        if self.head >= len(self.data):
            self.head = 0
        return t

    def pop_back(self) -> int:
        prev = self.tail - 1
        if prev < 0:
            prev = len(self.data)
        else:
            t = self.data[prev]
            self.data[prev] = 0
            self.tail = prev
            return t