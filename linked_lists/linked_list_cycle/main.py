# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head == 1e6:
                return True
            head.val = 1e6
            head = head.val
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if fast == head:
                return True
        return False