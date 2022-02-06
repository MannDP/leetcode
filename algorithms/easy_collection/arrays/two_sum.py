from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in index_map:
                return idx, index_map[diff]
            else:
                index_map[value] = idx
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
print(s.twoSum([3, 3], 7))
