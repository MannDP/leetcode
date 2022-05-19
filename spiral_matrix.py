from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        left_col, right_col = 0, n - 1
        top_row, bot_row = 0, m - 1
        result = []
        while left_col <= right_col and top_row <= bot_row:
            for i in range(left_col, right_col + 1):
                result.append(matrix[top_row][i])
            
            for i in range(top_row + 1, bot_row + 1):
                result.append(matrix[i][right_col])

            if top_row != bot_row:
                for i in range(right_col - 1, left_col - 1, -1):
                    result.append(matrix[bot_row][i])
            
            if left_col != right_col:
                for i in range(bot_row - 1, top_row, -1):
                    result.append(matrix[i][left_col])

            left_col += 1
            top_row += 1
            right_col -= 1
            bot_row -= 1
        return result

s = Solution()
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(s.spiralOrder([[6,9,7]]))
