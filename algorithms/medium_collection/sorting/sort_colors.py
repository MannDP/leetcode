class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums) - 1

        index = 0
        while index <= p2:
            num = nums[index]
            if num == 0:
                nums[p0], nums[index] = nums[index], nums[p0]
                p0 += 1
                index += 1
            elif num == 2:
                nums[p2], nums[index] = nums[index], nums[p2]
                p2 -= 1
            else:
                index += 1
