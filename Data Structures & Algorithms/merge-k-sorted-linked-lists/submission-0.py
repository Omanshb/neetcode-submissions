# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
            start = ListNode()
            curr = start
            while (list1 and list2):
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            curr.next = list1 or list2
            return start.next
        
        while len(lists) > 1:
            list1 = lists.pop()
            list2 = lists.pop()
            newList = merge2Lists(list1, list2)
            lists.append(newList)
        
        if len(lists) == 0:
            return None
        return lists[0]
