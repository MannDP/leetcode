from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0
        fast_ptr = 1
        while fast_ptr < len(nums):
            if nums[k] == nums[fast_ptr]:
                fast_ptr += 1
                continue
            k = k + 1
            nums[k] = nums[fast_ptr]
        return k + 1

    def leetcode_optimal(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

s = Solution()

test_case = [1,1,2]
soln = s.remove_duplicates(test_case)
print(test_case[0:soln])

test_case = [0,0,1,1,1,2,2,3,3,4]
soln = s.remove_duplicates(test_case)
print(test_case[0:soln])

test_case = []
soln = s.remove_duplicates(test_case)
print(test_case[0:soln])
