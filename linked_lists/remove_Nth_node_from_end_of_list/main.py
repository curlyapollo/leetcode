# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        data = []
        cur = head
        while cur:
            data.append(cur)
            cur = cur.next
        if len(data) == 1:
            return None
        if len(data) == n:
            return data[1]
        if n > 1:
            data[len(data) - n - 1].next = data[len(data) - n + 1]
        else:
            data[len(data) - n - 1].next = None
        data.pop(-n)
        return data[0]

    def another(self, head, n):
        dummy = ListNode()
        dummy.next = head

        pnt1, pnt2 = dummy, head
        for _ in range(n):
            pnt2 = pnt2.next

        while pnt2:
            pnt1, pnt2 = pnt1.next, pnt2.next

        pnt1.next = pnt1.next.next
        return dummy.next