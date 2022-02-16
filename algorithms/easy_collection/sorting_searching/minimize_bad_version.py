# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # binary search
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        # solution is guaranteed to exist
        while True:
            middle = left + (left + right) // 2
            middle_bad = isBadVersion(middle)
            if not middle_bad:
                left = middle + 1
            else:
                if not isBadVersion(middle - 1):
                    return middle
                right = middle - 1



        return binary_search(0, n)