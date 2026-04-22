# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr and counter < k:
            curr = curr.next
            counter += 1
        
        if counter == k:
            curr = self.reverseKGroup(curr, k)
            while counter > 0:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                counter -= 1
            head = curr
        return head





                