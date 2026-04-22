# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        right = []
        curr = head
        while curr:
            right.append(curr)
            curr = curr.next
        
        lnth = len(right)
        dummy = curr = ListNode()
        for i in range(lnth):
            if i % 2 == 0:
                curr.next = head
                head = head.next
            else:
                curr.next = right[-1]
                right.pop()
            curr = curr.next
            curr.next = None
        head = dummy.next

        