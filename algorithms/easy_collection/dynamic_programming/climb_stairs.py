class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases?
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        # start from n = 4
        one_below, two_below = 3, 2
        for i in range(4, n):
            tmp = two_below
            two_below = one_below
            one_below += tmp
        return one_below + two_below
