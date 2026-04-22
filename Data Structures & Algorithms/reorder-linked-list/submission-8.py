# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Just get to middle of list with fast/slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of the list
        second = slow.next
        slow.next = None
        
        p = None
        while second:
            n = second.next
            second.next = p
            p = second
            second = n
        
        # merge second half list into first half
        first, second = head, p
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2