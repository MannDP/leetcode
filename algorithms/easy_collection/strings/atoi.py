from typing import List


class Solution:
    def myAtoi(self, s: str) -> int:
        # trim leading whitespace
        s = s.strip()

        if not s:
            return 0

        # read the sign if provided
        factor = -1 if s[0] == '-' else 1

        # strip off sign digit
        if s[0] == '+' or s[0] == '-':
            s = s[1:]

        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break

        if not s:
            return 0

        result = int(s) * factor
        if result > (2 ** 31 - 1):
            return (2 ** 31 - 1)
        elif result < (2 ** 31 * -1):
            return (2 ** 31 * -1)
        else:
            return result


s = Solution()
print(s.myAtoi("+1"))
print(s.myAtoi("42"))
print(s.myAtoi("   -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("2147483648"))
print(s.myAtoi("-2147483648"))
print(s.myAtoi("words and 987"))
