class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        # base cases, starting level 3
        n_minus_one, n_minus_two = 2, 1
        for i in range(3, n):
            curr_level = n_minus_one + n_minus_two
            n_minus_two = n_minus_one
            n_minus_one = curr_level
        return n_minus_one + n_minus_two
