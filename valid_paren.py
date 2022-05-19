class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dict = {'}': '{', ')': '(', ']': '['}
        for char in list(s):
            if char not in paren_dict:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != paren_dict[char]:
                    return False
        return len(stack) == 0
