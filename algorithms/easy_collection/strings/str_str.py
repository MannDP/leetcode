class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("", ""))
