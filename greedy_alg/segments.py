class Segment:
    def __init__(self, l, r):
        self.l = l
        self.r = r


def solve(segments: list[Segment]) -> int:
    if not segments:
        return 0
    segments.sort(key=lambda x: x.r)
    last_r = segments[0].l
    ans = 0
    for i in segments:
        if i.l >= last_r:
            ans += 1
            last_r = i.r
    return ans
