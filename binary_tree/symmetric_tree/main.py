# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymm(self, leftBranch, rightBranch):
        if not leftBranch and not rightBranch:
            return True
        if not leftBranch or not rightBranch or leftBranch.val != rightBranch.val \
                or not self.isSymm(leftBranch.left, rightBranch.right) or not self.isSymm(leftBranch.right, rightBranch.left):
            return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isSymm(root.left, root.right)

