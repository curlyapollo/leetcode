# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root, ans):
            if root:
                ans = dfs(root.left, ans)
                ans = dfs(root.right, ans)
                if low <= root.val <= high:
                    ans += root.val
            return ans
        return dfs(root, 0)