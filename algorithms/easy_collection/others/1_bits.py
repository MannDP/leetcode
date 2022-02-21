class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1
        return count
    

s = Solution()
print(s.hammingWeight(11))
print(s.hammingWeight(128))
print(s.hammingWeight(4294967293))
