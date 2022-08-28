# O(n), O(n)
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_sums = {0 : 1}
        
        running = 0
        res = 0
        for n in nums:
            running += n
            remain = running % k
            if remain in prefix_sums:
                res += prefix_sums[remain]
                prefix_sums[remain] += 1
            else:
                prefix_sums[remain] = 1
        return res
