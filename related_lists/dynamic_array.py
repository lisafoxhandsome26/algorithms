from array import array


class DynArray:

    def __init__(self):
        self.data: array = array('i', (0 for _ in range(1)))
        self.length = 0

    def size(self) -> int:
        return self.length

    def sett(self, ind: int, value: int) -> None:
        self.data[ind] = value

    def get(self, ind: int) -> int:
        return self.data[ind]

    def add(self, x: int) -> None:
        lenn = len(self.data)
        if self.length == lenn:
            data2: array = array('i', (0 for _ in range(self.length * 2)))
            for i in range(0, self.length):
                data2[i] = self.data[i]

            self.data = data2

        self.data[self.length] = x
        self.length += 1

    def remove(self) -> None:
        lenn = len(self.data)
        self.length -= 1
        if self.length * 4 <= lenn:
            data2: array = array('i', (0 for _ in range(self.length // 2)))
            for i in range(len(self.data)):
                data2[i] = self.data[i]

            self.data = data2

    def insert(self, x: int, ind: int) -> None:
        self.add(0)
        for i in range(self.length-1, ind, -1):
            self.data[i] = self.data[i-1]

        self.data[ind] = x
