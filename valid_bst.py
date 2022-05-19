from typing import Optional, Tuple

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # analysis O(n) time, O(1) space
    # top-down checking with inline function definition
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(node, left, right) -> bool:
            if not node:
                return True
            if not node.val > left or not node.val < right:
                return False
            return solve(node.left, left, node.val) and solve(node.right, node.val, right)
        return solve(root, float('-inf'), float('inf'))

    # analysis O(n) and O(n) space
    # def in_order_traverse(self, root: Optional[TreeNode], vals: List[int]) -> None:
        # if not root:
        #     return
        # self.in_order_traverse(root.left, vals)
        # vals.append(root.val)
        # self.in_order_traverse(root.right, vals)

s = Solution()
three = TreeNode(val=3)
six = TreeNode(val=6)
four = TreeNode(val=4, left=three, right=six)
one = TreeNode(val=1)
five = TreeNode(val=5, left=one, right=four)
print(s.isValidBST(five))
