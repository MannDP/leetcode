# Given an array of n distinct integers, and an integer threshold, how many (a,b,c) index triplets exists that satisfy both of the following conditions?
# arr[a] < arr[b] < arr[c]
# arr[a] + arr[b] + arr[c] <= t

# time: O(n^2), space: O(1)
from typing import List

def triplets(arr: List[int], t: int) -> int:
    arr.sort()
    res = 0
    for i in range(len(arr) - 2):
        res += two_sum(arr, i + 1, t - arr[i])
    return res


def two_sum(arr: List[int], start: int, target: int) -> int:
    res = 0
    l, r = start, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] <= target:
            res += r - l
            l += 1
            continue
        r -= 1
    return res


print(triplets([1, 2, 3, 4, 5], 8) == 4)
print(triplets([1, -1, 2, -2, 3, -3, 4, -4], 0) == 30)
print(triplets([-2, 5, 2, 4, -3, 1, -5], -1) == 13)
print(triplets([1, 1, 1, 1, 1], 3) == 10)
