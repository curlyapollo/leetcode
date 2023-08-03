# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hist = {}
        ans = []
        def dfs(root: Optional[TreeNode]) -> str:
            if not root:
                return "#"
            s = ""
            s += str(root.val) + "." + dfs(root.left) + "." + dfs(root.right)
            if s in hist:
                hist[s] += 1
                if hist[s] == 2:
                    ans.append(root)
            else:
                hist[s] = 1
            return s
        dfs(root)
        return ans