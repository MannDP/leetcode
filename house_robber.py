from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = prev_prev = 0
        for loot in nums:
            max_profit = max(prev_prev + loot, prev)
            prev_prev = prev
            prev = max_profit
        return prev
