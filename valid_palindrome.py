class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = str(''.join(filter(lambda v: (v.isalnum()), s)).lower())
        return s == s[::-1]
        


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
