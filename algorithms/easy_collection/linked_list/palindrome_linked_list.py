from turtle import forward
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(n) and O(1) by reversing the second half of the linked list
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # single node is valid palindrome
        if not head.next:
            return True

        # need the length of the linked list
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next

        # reverse the second half of the linked list
        reverse_ptr = self.reverse_second_half(head, length)

        # compare
        forward_ptr = head
        while True:
            if forward_ptr.val != reverse_ptr.val:
                return False
            if forward_ptr.next == reverse_ptr or forward_ptr == reverse_ptr:
                return True
            forward_ptr = forward_ptr.next
            reverse_ptr = reverse_ptr.next
    
    def reverse_second_half(self, head: ListNode, n: int) -> ListNode:
        offset = n // 2 + n % 2
        first_half_last = head
        for _ in range(offset - 1):
            first_half_last = first_half_last.next
        
        prev = first_half_last.next
        nxt = prev.next
        prev.next = first_half_last

        # there is nothing to reverse
        if n == 3:
            return prev

        # reverse the list
        while nxt:
            tmp = nxt.next
            nxt.next = prev
            prev = nxt
            nxt = tmp
        return prev


s = Solution()

