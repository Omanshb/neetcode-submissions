# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        curr = start
        while (list1 or list2):
            if list1 and list2:
                if list1.val <= list2.val:
                    temp = list1.next
                    list1.next = None
                    curr.next = list1
                    curr = curr.next
                    list1 = temp
                else:
                    temp = list2.next
                    list2.next = None
                    curr.next = list2
                    curr = curr.next
                    list2 = temp
            else:
                if list1:
                    while list1:
                        temp = list1.next
                        list1.next = None
                        curr.next = list1
                        curr = curr.next
                        list1 = temp
                else:
                    while list2:
                        temp = list2.next
                        list2.next = None
                        curr.next = list2
                        curr = curr.next
                        list2 = temp
        return start.next
                