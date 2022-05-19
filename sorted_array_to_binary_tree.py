from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            middle = (right - left) // 2 + left
            root = TreeNode(val=nums[middle])
            root.left = solve(left, middle - 1)
            root.right = solve(middle + 1, right)
            return root

        # create root node to return
        return solve(0, len(nums) - 1)


s = Solution()
root = s.sortedArrayToBST([-10, -3, 0, 5, 9])
print(root.val)
print(root.left.val, root.right.val)
print(root.left.left, root.left.right.val, root.right.left, root.right.right.val)
