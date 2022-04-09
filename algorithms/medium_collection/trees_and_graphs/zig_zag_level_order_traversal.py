# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.build_lists(root, 0, res)
        return res

    def build_lists(self, root: Optional[TreeNode], depth: int, depth_lists: List[deque[int]]) -> None:
        if not root:
            return
        if depth == len(depth_lists):
            depth_lists.append(deque())

        if depth % 2 == 1:
            depth_lists[depth].insert(0, root.val)
        else:
            depth_lists[depth].append(root.val)

        self.build_lists(root.left, depth + 1, depth_lists)
        self.build_lists(root.right, depth + 1, depth_lists)
