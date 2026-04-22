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

"""
Intuition: This problem is essentially just broken into three discrete steps. Step 1 
is to break the list up into halves. You do this using fast and slow pointers. Step 2
is to reverse the second half of the list. Step 3 is to merge the first half and 
that reversed second half so that you get the reordered list.

Time Complexity: O(n)
Space Complexity: O(1)
"""
