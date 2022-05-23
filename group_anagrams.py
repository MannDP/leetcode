from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        def to_rep(s: str) -> str:
            return "".join(sorted(s))

        for s in strs:
            rep = to_rep(s)
            if rep not in groups:
                groups[rep] = []
            groups[rep].append(s)
        return groups.values()



