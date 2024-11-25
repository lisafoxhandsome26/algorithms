class User:
    def __init__(self, ident: int, name: str, age: int) -> None:
        self.ident = ident
        self.name = name
        self.age = age

    def compareTo(self, s) -> int:
        if self.age == s.age and self.name == s.name:
            return 0
        if self.age == s.age:
            if self.name < s.name:
                return -1
            else:
                return 1
        else:
            if self.age < s.age:
                return -1
            else:
                return 1

    def compareTo2(self, s) -> int:
        if compare(self, s):
            return -1
        if compare(s, self):
            return 1
        return 0

        
def compare(a: User, b: User) -> bool:
    return a.ident < b.ident


def compare2(a: User, b: User) -> bool:
    if a.age != b.age:
        return a.age < b.age
    else:
        return a.name < b.name
