"""Алгоритм бинарного поиска"""


def find_element(ages: list[int], element: int) -> str:
    ages = sorted(ages)

    left: int = 0
    right: int = len(ages) - 1

    while left <= right:
        middle: int = (left + right) // 2
        if ages[middle] < element:
            left = middle + 1
        elif ages[middle] > element:
            right = middle - 1
        else:
            return f"element {element} was found"
    return f"element {element} das not exists"


if __name__ == "__main__":
    ages: list[int] = [5, 45, 23, 10, 12, 1, 65, 15, 69]
    element: int = 23
    result: str = find_element(ages, element)
    print(result)
