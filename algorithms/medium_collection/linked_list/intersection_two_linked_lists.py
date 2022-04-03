from re import X
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        
        while pA != pB:
            pA = headB if not pA else pA.next
            pB = headA if not pB else pB.next
        
        return pA