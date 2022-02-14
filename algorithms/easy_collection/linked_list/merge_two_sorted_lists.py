from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if not list2:
            return list1
        elif not list1:
            return list2

        head = list1 if list1.val < list2.val else list2
        current = head
        while list1 or list2:
            if not list1:
                current.next = list2
                break
            elif not list2:
                current.next = list1
                break
            else:
                if list1.val < list2.val:
                    next = list1
                    list1 = list1.next
                else:
                    next = list2
                    list2 = list2.next
                current.next = next
                current = next
        return head
