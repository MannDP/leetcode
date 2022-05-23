from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length
        for update in updates:
            start, end, inc = update
            result[start] += inc
            if end < length - 1:
                result[end + 1] -= inc
        
        delta = result[0]
        for i in range(1, length):
            result[i], delta = delta, delta + result[i]
        return result
