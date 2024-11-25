# Код который проверяет, является ли массив отсортированным O(n)
def isSorted(a: list[int]) -> bool:
    for i in range(0, len(a) - 1):
        if a[i] > a[i+1]:
            return False
    return True


# Пузырьковая сортировка в виде двух функций с использованием isSorted
def trySort(a: list[int]) -> None:
    for i in range(0, len(a)-1):
        if a[i] > a[i+1]:
            c = a[i]
            a[i] = a[i+1]
            a[i+1] = c


def sort(a: list[int]) -> None:
    while not isSorted(a):
        trySort(a)


# Оптимизированный код пузырьковый сортировки
def bubleSort(a: list[int]) -> None:
    f = True
    for j in range(0, len(a)):
        f = False
        for i in range(0, len(a)-1-j):
            if a[i] > a[i+1]:
                c = a[i]
                a[i] = a[i+1]
                a[i+1] = c
                f = True

        if not f:
            break
