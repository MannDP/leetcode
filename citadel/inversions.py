from typing import List

# O(n^2) idea, but there is a faster one, https://leetcode.com/discuss/interview-question/1807872/tiktok-oa-find-length-3-of-inversions-in-list
def max_inversions(prices: List[int]) -> int:
    ans = 0
    for i, price in enumerate(prices):
        count_left = len([x for x in prices[:i] if x > price])
        count_right = len([x for x in prices[i:] if x < price])
        ans += count_left * count_right
    return ans
