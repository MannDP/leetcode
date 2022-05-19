from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_tail = res_head = ListNode(-1)

        carry = 0
        while l1 or l2 or carry:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += carry
            carry = val // 10
            val %= 10
                
            digit_node = ListNode(val)
            res_head.next = digit_node
            res_head = digit_node
        
        return res_tail.next
