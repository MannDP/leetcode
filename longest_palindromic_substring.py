from re import L


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l_idx = r_idx = i

            # odd length palindromes
            while l_idx >= 0 and r_idx < len(s) and s[l_idx] == s[r_idx]:
                if r_idx - l_idx + 1 > len(res):
                    res = s[l_idx : r_idx + 1]
                l_idx -= 1
                r_idx += 1
            
            # even length palindromes
            l_idx, r_idx = i, i + 1
            while l_idx >= 0 and r_idx < len(s) and s[l_idx] == s[r_idx]:
                if r_idx - l_idx + 1 > len(res):
                    res = s[l_idx : r_idx + 1]
                l_idx -= 1
                r_idx += 1
        return res


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalinrome("cbbd"))
