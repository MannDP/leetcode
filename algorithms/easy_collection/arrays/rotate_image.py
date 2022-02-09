from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for row in range(N // 2 + N % 2):
           for col in range(row, N - 1 - row):
               tmp = matrix[row][col]
               matrix[row][col] = matrix[N - 1 - col][row]
               matrix[N - 1 - col][row] = matrix[N - 1 - row][N - 1 - col]
               matrix[N - 1 - row][N - 1 - col] = matrix[col][N - 1 - row]
               matrix[col][N - 1 - row] = tmp



s = Solution()
test_cases = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [
    [5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]]
for test_case in test_cases:
    s.rotate(test_case)
    print(test_case)
