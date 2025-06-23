# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # approach:
        # count number of nodes
        # count index of middle node
        # remove middle node by pointing previous node to next node

        count = 0
        temp = head

        while temp != None:
            count += 1

            temp = temp.next

        middle_i = count // 2
        i = 0

        curr = head
        prev = None

        while i != middle_i:
            prev = curr
            curr = curr.next

            i += 1

        if prev:
            prev.next = curr.next
        else:
            head = None

        return head