# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        fast, slow = head, head
        # slow -- серединка
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # перевернем вторую половину
        prev = None
        cur = slow
        while cur:
            nexxt = cur.next
            cur.next = prev
            prev = cur
            cur = nexxt
        # сверим половинки
        ptr1 = head
        ptr2 = prev
        while ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return True