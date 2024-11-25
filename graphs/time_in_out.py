# Время входа и время выхода
def dfs1_count(x, depth, p: int) -> int:
    global T
    t_in[x] = T
    T += 1
    d[x] = depth
    weight = 1
    for i in range(0, len(v[x])):
        a = v[x][i]
        if a == p:
            continue
        weight += dfs1_count(a, depth+1, x)
    w[x] = weight
    t_out[x] = T
    T += 1
    return weight


def dfs_count(x: int) -> None:
    dfs1_count(x, 0, -1)


n = 5
root = 3
w, v, d = [], [], []
t_in = [0] * n
t_out = [0] * n
T = 0
r = dfs_count(root)
print(r)


def is_in_subtree(a, b: int) -> bool:
    if t_in[b] < t_in[a]:
        return False
    if t_out[b] > t_out[a]:
        return False
    return True
