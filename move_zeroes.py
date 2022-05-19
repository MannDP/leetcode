from cgi import test
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        offset = 0
        idx = 0
        while idx + offset < len(nums):
            next = nums[idx + offset]
            if next == 0:
                offset += 1
            else:
                nums[idx] = next
                idx += 1

        for i in range(len(nums) - offset, len(nums)):
            nums[i] = 0


s = Solution()
test_case = [0, 1, 0, 3, 12]
s.moveZeroes(test_case)
print(test_case)

test_case = [0]
s.moveZeroes(test_case)
print(test_case)
