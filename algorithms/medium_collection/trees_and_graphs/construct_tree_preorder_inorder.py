"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftmost = root
        while leftmost.left:
            # establish connections for next level
            level_iter = leftmost
            while level_iter:
                level_iter.left.next = level_iter.right
                if level_iter.next:
                    level_iter.right.next = level_iter.next.left
                level_iter = level_iter.next
            leftmost = leftmost.left
        return root
