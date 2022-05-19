from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zero_first_row = zero_first_col = False
        for row in range(m):
            if matrix[row][0] == 0:
                zero_first_col = True
        for col in range(n):
            if matrix[0][col] == 0:
                zero_first_row = True

        # iterate top to bottom, left to right
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    # mark row, mark column
                    matrix[row][0] = matrix[0][col] = 0

        # zero out rows
        for row in range(1, m):
            if matrix[row][0] == 0:
                matrix[row] = [0] * n
        # zero out columns
        for col in range(1, n):
            if matrix[0][col] == 0:
                for row in range(m):
                    matrix[row][col] = 0

        if zero_first_row:
            matrix[0] = [0] * n

        if zero_first_col:
            for row in range(m):
                matrix[row][0] = 0


s = Solution()
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# s.setZeroes(matrix)
# print(matrix)

# matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# s.setZeroes(matrix)
# print(matrix)

matrix = [
    [3, 5, 5, 6, 9, 1, 4, 5, 0, 5],
    [2, 7, 9, 5, 9, 5, 4, 9, 6, 8],
    [6, 0, 7, 8, 1, 0, 1, 6, 8, 1],
    [7, 2, 6, 5, 8, 5, 6, 5, 0, 6],
    [2, 3, 3, 1, 0, 4, 6, 5, 3, 5],
    [5, 9, 7, 3, 8, 8, 5, 1, 4, 3],
    [2, 4, 7, 9, 9, 8, 4, 7, 3, 7],
    [3, 5, 2, 8, 8, 2, 2, 4, 9, 8]]
s.setZeroes(matrix)
print(matrix)
