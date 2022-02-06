class Solution:
    def checkString(self, s: str) -> bool:
        for idx in range(len(s) - 1):
            if s[idx] == 'b' and s[idx + 1] == 'a':
                return False
        return True

    def checkStringOld(self, s: str) -> bool:
        bSeen = False
        for char in s:
            if char == 'b':
                bSeen = True
            elif char == 'a' and bSeen:
                return False
        return True

s = Solution()
assert(s.checkString('a'))
assert(s.checkString('aaaaa'))
assert(s.checkString('aaaaabbbb'))
assert(not s.checkString('ba'))
assert(not s.checkString('aba'))
assert(not s.checkString('abab'))
