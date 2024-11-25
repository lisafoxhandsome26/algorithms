class DLList:
    class Node:
        def __init__(self, x) -> None:
            self.x = x
            self.prevNode = None
            self.nextNode = None

    def __init__(self) -> None:
        self.start = DLList.Node(None)
        self.end = DLList.Node(None)

    def print_dllist(self) -> None:
        t = self.start
        while t is not None:
            print(t.x + " ")
        print("")

    def push_front(self, x: int) -> None:
        t = DLList.Node(x)
        if self.start is None:
            self.start = t
            self.end = t
            return

        t.nextNode = self.start
        self.start.prevNode = t
        self.start = t

    def insert(self, v: Node, x: int) -> None:
        t = DLList.Node(x)
        next_el = v.nextNode
        if next_el is None:
            t.nextNode = None
            v.nextNode = t
            t.prevNode = v
            self.end = t
            return

        next_el.prevNode = t
        t.nextNode = next_el
        v.nextNode = t
        t.prevNode = v

    def push_back(self, x: int) -> None:
        if self.end is None:
            t = DLList.Node(x)
            self.start = t
            self.end = t
            return
        DLList.insert(self, self.end, x)

    def delete(self, v: Node) -> None:
        nextt = v.nextNode
        prev = v.prevNode

        if nextt is not None:
            prev.nextNode = nextt

        if prev is not None:
            nextt.prevNode = prev

        v.nextNode = None
        v.prevNode = None

        if v == self.start:
            self.start = nextt

        if v == self.end:
            self.end = prev

    def pop_front(self) -> None:
        DLList.delete(self, self.start)

    def pop_back(self) -> None:
        DLList.delete(self, self.end)

    def merge(self, l) -> None:
        if l.start is None:
            return
        if self.end is None:
            self.start = l.start
            self.end = l.end

        self.end.nextNode = l.start
        l.start.prevNode = self.end
        self.end = l.end

    def revert_rec(self, v: Node) -> None:
        """Рекурсивный разворот"""
        if v is None:
            return None
        t = self.revert_rec(v.nextNode)
        if t is not None:
            t.nextNode = v
        v.prevNode = t

    def revert_slow(self) -> None:
        tmp = self.revert_rec(self.start)
        tmp.nextNode = None
        t = self.start
        self.start = self.end
        self.end = t

    def revert(self) -> None:
        if self.start is None:
            return
        a = self.start
        b = self.start.nextNode
        a.nextNode = None
        if b is None:
            return
        c = b.nextNode
        while b is not None:
            b.nextNode = a
            a.prevNode = b
            a = b
            b = c
            if c is not None:
                c = c.nextNode
        a.prevNode = None
        t = self.start
        self.start = self.end
        self.end = t

    def find_cycle(self) -> None:
        a = self.start
        b = self.start
        while True:
            if b is None:
                break
            b = b.nextNode
            if a == b:
                break
            if b is None:
                break
            b = b.nextNode
            if a == b:
                break
            a = a.nextNode

        if b is None:
            print("Нет циклов")
            return
        while a != b:
            print(b.x, end=" ")
            b = b.nextNode
        print(b.x)
        print("")
