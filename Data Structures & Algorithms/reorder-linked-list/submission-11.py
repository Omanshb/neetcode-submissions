# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = slow.next
        slow.next = None

        prev = None
        while secondHalf:
            nxt = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = nxt
        
        secondHalf = prev
        firstHalf = head
        while secondHalf:
            n1, n2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = n1
            firstHalf = n1
            secondHalf = n2