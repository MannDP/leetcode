from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = 0

        for row in bank:
            count = row.count('1')
            if count:
                if prev:
                    result += prev * count
                prev = count
        return result


s = Solution()
print(s.numberOfBeams(["011001","000000","010100","001000"]))
print(s.numberOfBeams(["000","111","000"]))
