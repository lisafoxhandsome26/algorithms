import random

class Node:
    def __init__(self, x, parent, l=None, r=None):
        self.x = x
        self.parent = parent
        self.l = l
        self.r = r


class Tree:
    def __init__(self):
        self.root = None

    def put(self, v, x):
        if v is None:
            return
        if x < v.x:
            if v.l is None:
                v.l = Node(x, parent=v)
                return
            self.put(v.l, x)
        else:
            if v.r is None:
                v.r = Node(x, parent=v)
                return
            self.put(v.r, x)

    def add(self, x: int) -> None:
        if self.root is None:
            self.root = Node(x, parent=None)
            return
        self.put(self.root, x)

    def find2(self, v: Node, x: int) -> Node:
        if v is None:
            return None
        if v.x == x:
            return v
        if v.x > x:
            return self.find2(v.l, x)
        else:
            return self.find2(v.r, x)

    def find(self, x: int) -> Node:
        return self.find2(self.root, x)

    def delete2(self, t: Node) -> None:
        if t is None:
            return
        if t.l is None or t.r is None:
            child = None
            if t.l is not None:
                child = t.l
            else:
                child = t.r

            if t == self.root:
                self.root = child
                if child is not None:
                    child.parent = None
            if t.parent.l == t:
                t.parent.l = child
                if child is not None:
                    child.parent = t.parent
            else:
                t.parent.r = child
                if child is not None:
                    child.parent = t.parent
        else:
            nxt = t.r
            while nxt.l is not None:
                nxt = nxt.l
            t.x = nxt.x
            self.delete(nxt)

    def delete(self, x: int) -> None:
        if self.root is None:
            return
        t = self.find(x)
        if t is None:
            return
        self.delete2(t)

    def next_node(self, v: Node) -> None:
        if v is None:
            return None
        if v.r is not None:
            nxt = v.r
            while nxt.l is not None:
                nxt = nxt.l
            return nxt
        nxt = v
        while nxt.parent is not None and nxt.parent.r is None:
            nxt = nxt.parent
        return nxt.parent

    def print_tree2(self, v: Node) -> None:
        if v is None: return
        self.print_tree2(v.l)
        print(v.x)
        self.print_tree2(v.r)

    def print_tree(self) -> None:
        self.print_tree2(self.root)

    def check2(self, v: Node, l, r: None) -> bool:
        if v is None: return True
        if l is not None and v.x < l: return False
        if r is not None and v.x > r: return False
        return self.check2(v.l, l, v.x) and self.check2(v.r, v.x, r)

    def check(self) -> bool:
        return self.check2(self.root, None, None)


def fromArray2(a: list[int], l, r: int) -> Node:
    if l + 1 > r:
        return None
    if l + 1 == r:
        return Node(a[1], None)
    m = (l + r) // 2
    t = Node(a[m], None)
    t.l = fromArray2(a, l, m)
    t.r = fromArray2(a, m + 1, r)
    if t.l is not None:
        t.l.parent = t
    if t.r is not None:
        t.r.parent = t
    return t


def fromArray(a: list[int]) -> "Tree":
    res = Tree()
    res.root = fromArray2(a, 0, len(a))
    return res


if __name__ == "__main__":
    f = [random.randint(i, 100) for i in range(10)]
    f.sort()
    print(f)
    tree = fromArray(f)
    tree.print_tree()
