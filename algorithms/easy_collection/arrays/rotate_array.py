from cgi import test
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # do it with constant space
        return self.reverse_approach(nums, k)

    def reverse_approach(self, nums: List[int], k: int) -> None:
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        return

    def reverse(self, nums: List[int], start_idx: int, end_idx: int) -> None:
        while start_idx < end_idx:
            tmp = nums[start_idx]
            nums[start_idx] = nums[end_idx]
            nums[end_idx] = tmp
            start_idx += 1
            end_idx -= 1
    
    
    def cyclic_shift(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if not k:
            return

        start_idx = count = 0

        while count != len(nums):
            # do the first iteration
            current_idx, next_idx = start_idx, (current_idx + k) % len(nums)
            
            # store current value and write through
            tmp = nums[next_idx]
            nums[next_idx] = nums[current_idx]
            count += 1
            current_idx = next_idx

            while current_idx != start_idx:
                next_idx = (current_idx + k) % len(nums)
                tmp2 = nums[next_idx]
                nums[next_idx] = tmp
                tmp = tmp2
                count += 1
                current_idx = next_idx
            start_idx += 1


s = Solution()
test_case = [1,2,3,4,5,6,7]
s.rotate(test_case, 3)
print(test_case)

test_case = [-1,-100,3,99]
s.rotate(test_case, 2)
print(test_case)
