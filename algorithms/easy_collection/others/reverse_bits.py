class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2::]
        bits = '0' * (32 - len(bits)) + bits
        bits = bits[::-1]
        return int(bits, 2)


s = Solution()
print(s.reverseBits(43261596))
print(s.reverseBits(4294967293))