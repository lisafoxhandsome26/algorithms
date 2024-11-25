"""Поиск уникальных элементов"""


class FindUniqElements:
    def __init__(self, array: list[int]) -> None:
        self.array = array

    def find_uniq_ages(self) -> list[int]:
        uniq_ages: list[int] = []

        for age in self.array:
            exist: bool = False

            for uniq in uniq_ages:
                if uniq == age:
                    exist = True
                    break

            if not exist:
                uniq_ages.append(age)

        return uniq_ages

    def find_uniq_ages_sort(self) -> list[int]:
        ages: list[int] = sorted(self.array)

        first_age: int = ages[0]
        uniq_ages: list[int] = []

        for i in range(1, len(ages)):
            if ages[i] != first_age:
                uniq_ages.append(first_age)
                first_age = ages[i]

        uniq_ages.append(first_age)
        return uniq_ages


if __name__ == "__main__":
    ages: list[int] = [5, 45, 45, 45, 12, 1, 1, 65, 15, 69, 69]
    a: FindUniqElements = FindUniqElements(ages)
    ages: list[int] = a.find_uniq_ages_sort()
    print(ages)
