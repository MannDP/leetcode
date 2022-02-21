from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum 1,... n = n(n+1)/2
        N = len(nums)
        expected_sum = int((N) / 2 * (N + 1))
        return expected_sum - sum(nums)


s = Solution()
print(s.missingNumber(nums=[3, 0, 1]))
print(s.missingNumber(nums=[0, 1]))
print(s.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
