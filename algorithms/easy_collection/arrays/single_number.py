from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

    def set_based(self, nums: List[int]) -> int:
        # O(n) time
        # O(n) space
        seen_set = set()
        for num in nums:
            if seen_set.__contains__(num):
                seen_set.remove(num)
            else:
                seen_set.add(num)
        return list(seen_set)[0]


s = Solution()
print(s.singleNumber([2, 2, 1]))
