from typing import List


class Solution:
    def isValidSoduku(self, board: List[List[str]]) -> bool:
        # validate rows
        for row in board:
            seen = set()
            for value in row:
                if value != '.':
                    if value in seen:
                        return False
                    else:
                        seen.add(value)

        # validate columns
        for colx in range(9):
            seen = set()
            for rowx in range(9):
                value = board[rowx][colx]
                if value != '.':
                    if value in seen:
                        return False
                    else:
                        seen.add(value)

        # validate each sub-grid
        for row_start_x in range(0, 7, 3):
            for col_start_x in range(0, 7, 3):
                seen = set()
                for row_offset in range(0, 3):
                    for col_offset in range(0, 3):
                        value = board[row_start_x +
                                      row_offset][col_start_x + col_offset]
                        if value != '.':
                            if value in seen:
                                return False
                            else:
                                seen.add(value)

        return True


s = Solution()
print(s.isValidSoduku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(s.isValidSoduku(
    [["8", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(s.isValidSoduku([
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
