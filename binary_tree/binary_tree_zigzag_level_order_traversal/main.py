# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        nodes.append(root)
        ans = []
        parity = 0
        while nodes:
            levels = []
            for i in range(len(nodes)):
                cur = nodes.popleft()
                if cur:
                    levels.append(cur.val)
                    nodes.append(cur.left)
                    nodes.append(cur.right)
            if levels:
                if parity % 2:
                    ans.append(levels[::-1])
                else:
                    ans.append(levels)
            parity += 1
        return ans