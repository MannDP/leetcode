from typing import List

# O(n), O(n)
def segments(space: List[int], x: int) -> int:
    # base case
    if x == 1:
        return min(space)


    def clean_deque(i: int) -> None:
        if deq and deq[0] == i - x:
            deq.popleft()

        while deq and space[i] < space[deq[-1]]:
            deq.pop()

    from collections import deque
    deq = deque()
    min_idx = 0
    for i in range(x):
        clean_deque(i)
        deq.append(i)
        if space[i] < space[min_idx]:
            min_idx = i
    res = space[min_idx]

    for i in range(x, len(space)):
        clean_deque(i)
        deq.append(i)
        if space[deq[0]] > res:
            res = space[deq[0]]
    return res

print(segments([8, 2, 4], 2) == 2)
print(segments([1, 2, 3, 1, 2], 1) == 3)
print(segments([1, 1, 1], 2) == 1)
