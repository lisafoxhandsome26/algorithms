class KeyValuePair:
    key: str
    value: str


class HashMap:
    def __init__(self):
        self.entries: list[None | KeyValuePair] = [None] * 8
        self.size = 8
        self.number_of_elements = 0

    def hash_function(self, key: str):
        return 0

    def add(self, key: str, value: str) -> None:
        index = self.find_good_index(key)
        self.entries[index] = KeyValuePair(key, value)
        self.number_of_elements += 1
        if self.number_of_elements == self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int) -> None:
        new_entries: list[None | str] = [None] * new_size
        for i in range(self.size):
            entry = self.entries[i]
            index = self.find_good_index(entry.key)
            new_entries[index] = entry

        self.entries = new_entries
        self.size = new_size

    def get(self, key: str) -> None | str:
        index = self.find_good_index(key)
        entry = self.entries[index]
        if entry is None:
            return None
        return entry.value

    def find_good_index(self, key: str) -> int:
        hashh = self.hash_function(key)
        index = hashh % self.size
        for i in range(self.size):
            probing_index = (index + i) % self.size
            entry = self.entries[probing_index]
            if entry is None or entry.key == key:
                return probing_index
