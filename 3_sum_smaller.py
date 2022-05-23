from typing import List


class Solution:
    # the trick here is the condition is the same as three distinct integers
    # reduction to O(n^2) by not iterating over all pairs
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            num = nums[i]
            count += self.two_sum_smaller(nums, target - num, i + 1)
        return count

    def two_sum_smaller(self, nums: List[int], target: int, start_idx: int) -> int:
        l, r = start_idx, len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] < target:
                count += r - l
                l += 1
                continue
            r -= 1
        return count
