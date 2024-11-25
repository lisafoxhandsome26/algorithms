# Функция обхода в глубину
def dfs1(x, depth, p: int) -> None:
    d[x] = depth
    for i in range(0, len(v[x])):
        a = v[x][i]
        if a == p:
            continue
        dfs1(a, depth+1, x)


def dfs(x: int) -> None:
    dfs1(x, 0, -1)


n = 5
root = 3
e, v, d = [], [], []
dfs(root)


# Функция подсчитывающая количество вершин в поддереве
def dfs1_count(x, depth, p: int) -> int:
    d[x] = depth
    weight = 1
    for i in range(0, len(v[x])):
        a = v[x][i]
        if a == p:
            continue
        weight += dfs1(a, depth+1, x)
    v[x] = weight
    return weight


def dfs_count(x: int) -> None:
    dfs1(x, 0, -1)


n = 5
root = 3
e, v, d = [], [], []
dfs_count(root)
