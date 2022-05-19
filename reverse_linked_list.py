from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty list or single element list
        if not head or not head.next:
            return head

        # use a stack to reverse the nodes
        prev = head
        curr = head.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # remove cycle
        head.next = None
        return prev


s = Solution()

n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print(s.reverseList(n1))
