class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get_value(idx: int):
            if idx < 0 or idx >= len(nums):
                return float('-inf')
            return nums[idx]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            left_val, mid_val, right_val = get_value(
                mid - 1), nums[mid], get_value(mid + 1)
            if left_val < mid_val and mid_val > right_val:
                return mid
            elif left_val < mid_val:
                left = mid + 1
            else:
                right = mid - 1
        return left
