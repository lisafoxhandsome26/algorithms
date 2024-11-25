import random

from queue import PriorityQueue

q = PriorityQueue()
if q.empty():
    print("Queue is empty")

q.put(1, block=False)
q.put(23)
q.put(10)
print(q.get())
print(q.get())
print(q.get())


class Box:
    def __init__(self, m, w):
        self.m = m
        self.w = w

    def __str__(self):
        return f"Вес коробки - {self.m}, Вес коробки который может выдержать {self.w}"


def solve(boxes: list[Box]) -> int:
    boxes.sort(key=lambda x: (x.w + x.m))
    q = []
    f = PriorityQueue()
    sum_w, cnt = 0, 0
    for i in range(0, len(boxes)):
        if boxes[i].m >= sum_w:
            cnt += 1
            sum_w += boxes[i].w
            q.append(boxes[i])
            q.sort(key=lambda x: x.w, reverse=True)
        else:
            if q.peek().w > boxes[i].w:
                sum_w -= q.pop().w
                q.pop()
                q.append(boxes[i])
                q.sort(key=lambda x: x.w, reverse=True)
                sum_w += boxes[i].w
    return cnt


def gen():
    test_data = []
    for i in range(10):
        w = random.randint(i, 10)
        m = random.randint(i, 10)
        test_data.append((m, w))
    return [Box(i[0], i[1]) for i in test_data]


# d = gen()
# r = solve(d)

# print("Количество коробок до алгоритма - ", len(d))
# print("Количество коробок после алгоритма - ", r)
# for i in d:
#     print(i)
# print("--------------")
# r = d.sort(key=lambda x: sum(x.w for i in d ))
# for i in d:
#     print(i)
