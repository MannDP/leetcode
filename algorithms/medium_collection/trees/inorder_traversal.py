# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root: Optional[TreeNode], collection: List[int]) -> None:
        if not root:
            return
        self.helper(root.left, collection)
        collection.append(root.val)
        self.helper(root.right, collection)
