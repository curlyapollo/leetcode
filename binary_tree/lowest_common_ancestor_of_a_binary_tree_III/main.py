class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node):
        a = p
        b = q
        while a != b:
            if a:
                a = a.parent
            else:
                a = q
            if b:
                b = b.parent
            else:
                b = p
        return a
