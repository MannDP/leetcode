from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        nums.sort()
        for i in range(len(nums)):
            prev = nums[i] - 1 if i == 0 else nums[i - 1]
            curr = nums[i]
            if curr > 0:
                break
            elif prev == curr:
                continue
            else:
                two_sums = self.two_sum(nums, i)
                for two_sum in two_sums:
                    three_sum = two_sum + [curr]
                    results.append(three_sum)
        return results

    def two_sum(self, nums: List[int], base_idx: int) -> List[List[int]]:
        target = -1 * nums[base_idx]
        start_idx = base_idx + 1
        end_idx = len(nums) - 1

        pairs = []
        while start_idx < end_idx:
            small, big = nums[start_idx], nums[end_idx]
            sum = small + big
            if sum < target:
                start_idx += 1
            elif sum > target:
                end_idx -= 1
            else:
                pairs.append([small, big])
                while start_idx < end_idx and nums[start_idx] == small:
                    start_idx += 1
        return pairs


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([]))
print(s.threeSum([0]))
