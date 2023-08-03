# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        nodes.append(root)
        ans = []
        while nodes:
            levels = []
            for i in range(len(nodes)):
                cur = nodes.popleft()
                if cur:
                    levels.append(cur.val)
                    nodes.append(cur.left)
                    nodes.append(cur.right)
            if levels:
                ans.append(levels)
        return ans