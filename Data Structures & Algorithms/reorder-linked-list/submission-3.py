# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        curr = head
        while curr:
            temp = curr.next
            curr.next = None
            lst.append(curr)
            curr = temp
        
        dummy = curr = ListNode()
        i = 0
        while lst:
            if i % 2 == 0:
                curr.next = lst[0]
                lst.pop(0)
            else:
                curr.next = lst[-1]
                lst.pop()
            curr = curr.next
            i += 1
        head = dummy.next

        