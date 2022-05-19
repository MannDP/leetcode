from typing import List, Mapping


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_map = dict()
        result = []

        for num in nums1:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1

        for num in nums2:
            if num in count_map:
                result.append(num)
                count_map[num] -= 1
        return result


s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
