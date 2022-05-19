from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # runtime O(n) time
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(root: Optional[TreeNode], other: Optional[TreeNode]) -> bool:
            if not root and not other:
                return True
            if not root and other or root and not other:
                return False
            if root.val != other.val:
                return False
            return solve(root.left, other.right) and solve(root.right, other.left)
        return solve(root.left, root.right)
