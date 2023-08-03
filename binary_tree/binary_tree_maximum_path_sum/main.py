# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        def dfs(node: TreeNode):
            if not node:
                return 0
            val1 = max(dfs(node.left), 0)
            val2 = max(dfs(node.right), 0)
            ans[0] = max(ans[0], val1 + val2 + node.val)
            return node.val + max(val1, val2)
        dfs(root)
        return ans[0]