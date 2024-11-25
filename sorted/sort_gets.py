# Вставка элемента на нужное место в отсортированном массиве
def insert_into_sorted(a: list[int], x: int) -> None:
    pt = len(a)
    for i in range(0, len(a)):
        if a[i] > x:
            pt = i
            break
    a.append(0)
    for i in range(len(a)-1, pt, -1):
        a[i] = a[i-1]
    a[pt] = x


# f = [1, 2, 3, 4, 5, 6]
# d = insert_into_sorted(f, 7)
# print(f)

# Сортировка вставками с использованием дополнительного массива
def sort(a: list[int]) -> None:
    t = []
    for i in range(0, len(a)):
        insert_into_sorted(t, a[i])
    for i in range(0, len(a)):
        a[i] = t[i]

# f = [1, 2, 3, 4, 5, 6, 10, 8, 5]
# d = sort(f)
# print(f)

def sort2(a: list[int]) -> None:
    for i in range(0, len(a)):
        c = a[i]
        pt = i
        while pt > 0 and a[pt-1] > c:
            a[pt] = a[pt - 1]
            pt -= 1
        a[pt] = c

f = [1, 2, 3, 4, 5, 6, 10, 8, 5]
d = sort2(f)
print(f)
