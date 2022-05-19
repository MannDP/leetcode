class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_value(i: int):
            if i < 0 or i >= len(nums):
                return target - 1
            return nums[i]

        def find_start() -> int:
            # binary search for ..., F, T ...
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                left_val, mid_val = get_value(mid - 1), nums[mid]

                if left_val != target and mid_val == target:
                    return mid
                elif mid_val >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        def find_end() -> int:
            # binary search for ... T, F, ...
            # binary search for ..., F, T ...
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                mid_val, right_val = nums[mid], get_value(mid + 1)

                if mid_val == target and right_val != target:
                    return mid
                elif mid_val > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        # two binary searches, for left and right termination conditions
        return [find_start(), find_end()]
