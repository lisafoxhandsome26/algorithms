"""Наивный алгоритм удаления дубликатов"""


def remove_duplicates(array: list[int]) -> int:
    i = 0
    length = len(array)

    while i < length:
        found = False
        for k in range(i+1, length):
            if array[i] == array[k]:
                found = True
                break

        if not found:
            i += 1
            continue

        for k in range(i+1, length):
            array[k-1] = array[k]
        length -= 1

    return length


if __name__ == '__main__':
    array = [15, 23, 20, 5, 15, 20, 15, 20]
    print("Original:", array)
    r = remove_duplicates(array)
    print("Unique:", array[:r])
