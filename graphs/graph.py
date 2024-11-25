class Node:
    def __init__(self, idd):
        self.idd = idd
        self.v = []

    def __repr__(self):
        return f"Node {self.idd}"


class Edge:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def first_save_data():
    n = 5
    e = []
    ar = []
    for i in range(0, n):
        ar.append(Node(i))
    for i in range(0, len(e)):
        a = e[i].a
        b = e[i].b
        ar[a].v.append(ar[b])
        ar[b].v.append(ar[a])

    for i in ar:
        print(f"Вершина - {i} - Ребра - {i.v}")


def second_save_data():
    n = 5
    e = []
    v = []
    for i in range(0, n):
        v.append([0])
    for i in range(0, len(e)):
        a = e[i].a
        b = e[i].b
        v[a].append(b)
        v[b].append(a)
    for i in v:
        print(f"Вершина - {i}")


second_save_data()
