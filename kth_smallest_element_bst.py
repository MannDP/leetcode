from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time: O(n), space: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       stack = []
       while True:
            while root:
               stack.append(root)
               root = root.left
            top = stack.pop()
            k -= 1
            if not k:
                return top.val
            else:
                root = top.right
           
