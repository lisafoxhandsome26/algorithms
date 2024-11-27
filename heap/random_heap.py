import random


class Node:
    def __init__(self, x):
        self.l = None
        self.r = None
        self.x = x
        self.rnd = random.choice([True, False])

    def merge(self, l: "Node", r: "Node") -> "Node" | None:
        if r is None: return r
        if l is None: return l
        if l.x > r.x:
            t = l
            l = r
            r = t

        if self.rnd:
            l.l = self.merge(l.l, r)
        else:
            l.r = self.merge(l.r, r)
        return l
