from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        MAX = (2 ** 31) // 10  # constant for limit check

        factor = -1 if x < 0 else 1
        tolerance = 1 if x < 0 else 0

        x = abs(x)
        result = 0
        while x > 0:
            digit = x % 10
            x = x // 10

            # bound checking here
            if result > MAX:
                return 0
            elif result == MAX and digit > 7 + tolerance:
                return 0
            else:
                result *= 10
                result += digit
        return result * factor


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(-120))
print(s.reverse(2 ** 31 - 1))
print(s.reverse(-1 * 2 ** 31))
