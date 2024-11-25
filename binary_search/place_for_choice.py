"""Поиск места для вставки"""


class Player:
    def __init__(self, rating: int, nick_name: str) -> None:
        self.rating = rating
        self.nick_name = nick_name


class Doka3:
    def __init__(self) -> None:
        self.ratings = [
            Player(1100, "Crowbar Freeman"),
            Player(1200, "London Mollarik"),
            Player(1600, "Raziel of Kain"),
            Player(1600, "Gwinter of Rivia"),
            Player(1600, "Slayer of Fate"),
            Player(3000, "Jon Know"),
            Player(4000, "Caius Cosades"),
        ]

    def find_spot(self, new_player: Player) -> int:
        left = 0
        right = len(self.ratings) - 1
        while left < right:
            middle = (left + right) // 2
            if self.ratings[middle].rating < new_player.rating:
                left = middle + 1
            else:
                right = middle
        return left


if __name__ == "__main__":
    rating = Doka3()
    spot = rating.find_spot(Player(1600, "Shmike"))
    print(spot)
