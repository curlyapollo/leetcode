# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur_depth):
            if not root:
                return cur_depth
            return max(dfs(root.right, cur_depth + 1), dfs(root.left, cur_depth + 1))
        return dfs(root, 0)