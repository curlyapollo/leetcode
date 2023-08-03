# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def height(self, root):
        if not root:
            return 0
        right_height = self.height(root.rihgt)
        if right_height == -1:
            return -1
        left_height = self.height(root.left)
        if left_height == -1:
            return -1
        if abs(right_height - left_height) > 1:
            return -1
        return max(right_height, left_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0