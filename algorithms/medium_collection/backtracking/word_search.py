class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def match(row: int, col: int, idx: int) -> bool:
            # out of range index
            nonlocal m, n
            if row < 0 or col < 0 or row >= m or col >= n:
                return False

            # mismatch
            if board[row][col] != word[idx]:
                return False

            # cannot re-use character
            orig = board[row][col]
            board[row][col] = '#'

            # complete match
            if idx == len(word) - 1:
                return True

            # recurse and combine
            search = match(row + 1, col, idx + 1) or match(row - 1, col, idx +
                                                           1) or match(row, col + 1, idx + 1) or match(row, col - 1, idx + 1)

            if not search:
                board[row][col] = orig
            return search

        m = len(board)
        n = len(board[0])
        for row in range(m):
            for col in range(n):
                if match(row, col, 0):
                    return True
        return False
