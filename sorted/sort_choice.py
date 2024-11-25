def sort_choice(a: list[int]) -> None:
    for i in range(0, len(a)):
        pt = i
        for j in range(i+1, len(a)):
            if a[j] < a[pt]:
                pt = j

        c = a[i]
        a[i] = a[pt]
        a[pt] = c
