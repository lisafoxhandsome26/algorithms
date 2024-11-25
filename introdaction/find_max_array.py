"""Поиск максимального элемента"""


class MaxValues:
    def __init__(self, top_ages: int, ages: list[int]) -> None:
        if top_ages > len(ages):
            raise ValueError("Variable top age must smaller then array")

        self.top_ages: int = top_ages
        self.ages: list[int] = ages

    def max_age(self, top_age) -> int:
        max_age = float("-inf")

        for age in self.ages:
            if top_age > age:
                max_age = max(max_age, age)

        return max_age

    def find_top_ages(self):
        top_age = float("inf")
        max_ages: list[int] = []

        for i in range(self.top_ages):
            current_age = self.max_age(top_age)
            top_age = current_age
            max_ages.append(top_age)

        return max_ages


if __name__ == "__main__":
    ages: list[int] = [5, 45, 23, 10, 12, 1, 65, 15, 69]
    top: int = 9
    a: MaxValues = MaxValues(top, ages)
    ages: list[int] = a.find_top_ages()
    print(ages)
