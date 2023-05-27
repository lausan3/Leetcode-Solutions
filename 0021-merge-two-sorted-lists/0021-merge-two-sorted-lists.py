# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        # create new linked list with least value and a pointer to it
        if list1.val < list2.val:
            ptr = returnList = ListNode(list1.val)
            list1 = list1.next
        else:
            ptr = returnList = ListNode(list2.val)
            list2 = list2.next

        # main loop to add sorted items
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ptr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ptr.next = ListNode(list2.val)
                list2 = list2.next
            ptr = ptr.next

        # adding remaining nodes
        while list1 != None:
            ptr.next = ListNode(list1.val)
            list1 = list1.next
            ptr = ptr.next

        while list2 != None:
            ptr.next = ListNode(list2.val)
            list2 = list2.next
            ptr = ptr.next
        
        return returnList