from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        parent = None
        while head.next:
            temp = head.next
            head.next = parent
            parent = head
            head = temp
        head.next = parent
        return head