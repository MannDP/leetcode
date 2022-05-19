from typing import List

mapping = {
    '1': (),
    '2': ('a', 'b', 'c'),
    '3': ('d', 'e', 'f'),
    '4': ('g', 'h', 'i'),
    '5': ('j', 'k', 'l'),
    '6': ('m', 'n', 'o'),
    '7': ('p', 'q', 'r', 's'),
    '8': ('t', 'u', 'v'),
    '9': ('w', 'x', 'y', 'z'),
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.helper(digits, 0, [])

    def helper(self, digits: str, index: int, strs: List[str]) -> List[str]:
        # base case
        if index == len(digits):
            return strs

        chars = mapping[digits[index]]

        if not strs:
            # create first entries
            for char in chars:
                strs.append(char)
        else:
            # update existing entries
            new_strs = []
            for str in strs:
                for char in chars:
                    new_strs.append(str + char)
            strs = new_strs
        return self.helper(digits, index + 1, strs)

s = Solution()
print(s.letterCombinations('23'))
