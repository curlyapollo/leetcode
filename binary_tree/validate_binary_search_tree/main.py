# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:

    def isValidBSTRecursion(self, root, minimum, maximum):
        if root.val >= maximum or root.val <= minimum:
            return False
        if not root.left:
            if not root.right:
                return True
            return root.right.val > root.val and self.isValidBSTRecursion(root.right, root.val, maximum)
        if not root.right:
            return root.left.val < root.val and self.isValidBSTRecursion(root.left, minimum, root.val)
        return root.right.val > root.val > root.left.val and self.isValidBSTRecursion(root.right, root.val, maximum) and self.isValidBSTRecursion(root.left, minimum, root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRecursion(root, -1e10, 1e10)