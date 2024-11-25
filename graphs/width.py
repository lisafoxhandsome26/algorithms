
def bfs(x: int) -> None:
    cur = []
    next_n = [x]
    D = 0
    visited = [False] * n
    while len(next_n) > 0:
        cur = next_n
        next_n = []
        for i in range(0, len(cur)):
            a = cur[i]
            visited[a] = True
            d[a] = D
            for j in range(0, len(v[a])):
                b = v[a][j]
                if visited[b]:
                    continue
                next_n.append(b)
        D += 1


d = []
v = []
n = 5
