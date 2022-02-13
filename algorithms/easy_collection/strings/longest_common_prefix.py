from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        idx = 0
        while True:
            char = ''
            for str in strs:
                # string is not long enough
                if idx >= len(str):
                    return strs[0][:idx]

                if char == '':
                    char = str[idx]
                elif str[idx] != char:
                    return strs[0][:idx]
            idx += 1


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))