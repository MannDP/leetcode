from typing import List


class Solution:
    # time = O(NKlogK), space = O(NK) for N = number of strings, K = length of longest string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for str in strs:
            rep = ''.join(sorted(str))
            if rep not in results:
                results[rep] = []
            results[rep].append(str)
        return list(results.values())


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
