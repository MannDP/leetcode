class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create count map
        count_map = {}
        for c in s:
            count_map[c] = count_map.get(c, 0) + 1

        # iterate over it again        
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))
