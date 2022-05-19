from typing import List


class Solution:
    # recursive decomposition
    def generateParenthesis(self, n: int) -> List[str]:
        # base case
        if n == 1:
            return ["()"]

        # sub-problem
        sp = self.generateParenthesis(n - 1)

        # combine to get actual result
        result = set()
        for paren in sp:
            result.add("()" + paren)
            for i in range(len(paren)):
                result.add(paren[0:i] + "()" + paren[i:])
        return list(result)

s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
