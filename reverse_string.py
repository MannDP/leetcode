from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

s = Solution()
test_case = ["h","e","l","l","o"]
s.reverseString(test_case)
print(test_case)
