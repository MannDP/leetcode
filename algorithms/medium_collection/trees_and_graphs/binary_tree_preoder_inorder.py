# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left, right) -> Optional[TreeNode]:
            nonlocal preorder_idx
            if left > right:
                return None

            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            root.left = array_to_tree(left, inorder_map[root.val] - 1)
            root.right = array_to_tree(inorder_map[root.val] + 1, right)
            return root

        preorder_idx = 0
        inorder_map = {}
        for idx, elem in enumerate(inorder):
            inorder_map[elem] = idx
        return array_to_tree(0, len(preorder) - 1)
