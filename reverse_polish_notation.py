from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        
        stack = []
        for token in tokens:
            if token not in op_map:
                stack.append(int(token))
                continue
            fn = op_map[token]
            right = stack.pop()
            left = stack.pop()
            stack.append(int(fn(left, right)))

        return stack.pop()

