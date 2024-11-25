class Node:
    def __init__(self, w, zero, one, c):
        self.w = w
        self.zero = zero
        self.one = one
        self.c = c


def dfs(x: "Node", res: list[int]) -> None:
    if x.zero is None:
        print("\nCode for " + x.c + ":")
        for i in range(0, len(res)):
            print(res[i], end="")
        return
    res.append(0)
    dfs(x.zero, res)
    res.pop()
    res.append(1)
    dfs(x.one, res)


def huffman(s: str) -> None:
    a = [0] * 256
    for i in range(0, len(s)):
        a[ord(s[i])] += 1
    q = []
    for i in range(0, 256):
        if a[i] > 0:
            q.append(Node(a[i], None, None, chr(i)))
    q.sort(key=lambda x: x.w, reverse=True)
    while len(q) > 1:
        print(q[-1].c)
        t1 = q.pop()
        t2 = q.pop()
        n = Node(t1.w + t2.w, t2, t1, '\0')
        q.append(n)
    dfs(q[0], [])


f = "abracadabra"
huffman(f)
