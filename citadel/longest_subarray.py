class Solution:
    def maxLength(self, nums: list[int], k: int) -> int:
        res = -1
        
        l = r = 0
        window_sum = 0
        while r < len(nums):
            num = nums[r]

            # special case, element is too large
            if num > k:
                window_sum = 0
                r += 1
                l = r
                continue
            
            # expand right
            window_sum += num
            # contract left, if needed
            while l < r and window_sum > k:
                window_sum -= nums[l]
                l += 1
            
            # update length
            res = max(res, r - l + 1)
            r += 1
        return res

s = Solution()
print(s.maxLength([1, 2, 3], 4))
print(s.maxLength([1,2,3], 4))
print(s.maxLength([3,1,2,1], 4))
print(s.maxLength([1,1,1,1,1,1], 6))
print(s.maxLength([9,1,1,1,1,1,1], 6))
print(s.maxLength([9,1,1,1,1,5,1,1], 6))
print(s.maxLength([9,1,1,1,1,2,1,1], 6))
