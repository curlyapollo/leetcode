from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(nlogn)
    def mergeKLists1(self, head: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Creating a list from the given LinkNode
        new = []
        for i in head:
            while i:
                new.append(i.val)
                i = i.next

        # Sort the list and reverse it
        a = sorted(new, reverse=True)

        # Create a ListNode from list
        final = None
        for i in a:
            final = ListNode(i, final)
        return final

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tmp = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]