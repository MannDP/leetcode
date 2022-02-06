class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return not num or num % 10 != 0


s = Solution()
assert(s.isSameAfterReversals(55))
assert(not s.isSameAfterReversals(1800))
assert(s.isSameAfterReversals(0))
