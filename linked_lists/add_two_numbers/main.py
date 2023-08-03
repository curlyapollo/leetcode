from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = l1.val + l2.val
        digit, tenth = sum % 10, sum // 10
        answer = ListNode(digit)
        if l1.next or l2.next or tenth:
            if not l1.next:
                l1 = ListNode(0)
            else:
                l1 = l1.next
            if not l2.next:
                l2 = ListNode(0)
            else:
                l2 = l2.next
            l1.val += tenth
            answer.next = self.addTwoNumbers(l1, l2)
        return answer