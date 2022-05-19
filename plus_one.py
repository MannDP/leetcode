from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        carry = 0

        while idx >= 0:
            if digits[idx] == 9:
                digits[idx] = 0
                carry = 1
            else:
                digits[idx] += 1
                carry = 0
                break
            idx -= 1

        if carry:
            digits.insert(0, 1)
        return digits


s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([9]))
