from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # runtime: O(n), space: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        aggregator = []
        def collect_nodes(root: Optional[TreeNode], aggregator: List[List[int]], depth: int) -> None:
            if not root:
                return
            while len(aggregator) < depth + 1:
                aggregator.append([])
            collect_nodes(root.left, aggregator, depth + 1)
            aggregator[depth].append(root.val)
            collect_nodes(root.right, aggregator, depth + 1)

        collect_nodes(root, aggregator, 0)
        return aggregator