def hanoi(n: int, fromm, to, aux: chr) -> None:
    if n == 1:
        print("Move from ", fromm, " to ", to)
        return
    hanoi(n-1, fromm, aux, to)
    print("Move from ", fromm, " to ", to)
    hanoi(n-1, aux, to, fromm)


hanoi(2, "A", "C", "B")
