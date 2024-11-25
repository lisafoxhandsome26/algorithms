class Node:

    def __init__(self, x):
        self.x: int = x
        self.next = None


if __name__ == "__main__":
    start = Node(None)
    t = start

    for i in range(0, 11):
        node: Node = Node(i)
        node.next = start
        start = node

    summ = 0

    while t.next is not None:
        summ += t.x
        t = t.next

