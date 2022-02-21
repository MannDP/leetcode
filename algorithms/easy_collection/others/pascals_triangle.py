from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # base cases
        result = list()
        result.append([1])
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result
        
        # now construct the lists
        for i in range(2, numRows):
            row_len = i + 1
            row = [1] * row_len
            for j in range(1, row_len - 1):
                row[j] = result[-1][j - 1] + result[-1][j]
            result.append(row)
        return result

s = Solution()
print(s.generate(5))
print(s.generate(1))
