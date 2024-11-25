def power(a: int, b: int) -> int: # O(N)
    """Возведение в степень O(N)"""
    if b == 0:
        return 1
    return a * power(a, b-1)


def power2(a: int, b: int) -> float: # O(logN)
    """Возведение в степень O(logN)"""
    if b == 0:
        return 1
    if b % 2 == 0:
        t = power2(a, b/2)
        return t * t
    else:
        return a * power2(a, b-1)


# Задача проверки на правильность скобочной последовательности с тремя видами скобок ()[]{}
def check(s: str) -> bool:
    st = []
    for c in s:
        if c in "([{":
            st.append(c)
        else:
            if not st:
                return False
            if c == ")" and st[-1] == "(":
                st.pop()
                continue
            if c == "]" and st[-1] == "[":
                st.pop()
                continue
            if c == "}" and st[-1] == "{":
                st.pop()
                continue
            return False

    if st:
        return False
    return True


class State:
    def __init__(self, a: int, b: int, st: int) -> None:
        self.a = a
        self.b = b
        self.st = st


def power3(a: int, b: int) -> int:
    """Возведение в степень при помощи стека"""
    st = []
    st.append(State(a, b, 0))
    ret = 0
    while st:
        a = st[-1].a
        b = st[-1].b
        pos = st[-1].st
        st.pop()
        if pos == 0:
            if b == 0:
                ret = 1
                continue
            if b % 2 == 0:
                st.append(State(a, b, 1))
                st.append(State(a, b/2, 0))
            else:
                st.append(State(a, b, 2))
                st.append(State(a, b-1, 0))
            continue
        elif pos == 1:
            ret = ret * ret
            continue
        else:
            ret = ret * a
            continue
    return ret


if __name__ == "__main__":
    res = check("[[[{{]]}}]")
    print(res)
    print(power3(2, 0))
