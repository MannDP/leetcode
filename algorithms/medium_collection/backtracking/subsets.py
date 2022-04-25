class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            length = len(results)
            for i in range(length):
                picked = results[i].copy()
                picked.append(num)
                results.append(picked)
        return results
