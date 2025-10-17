# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        carry = 0

        temp1, temp2, temp3 = l1, l2, res

        while temp1 or temp2:
            val1 = val2 = 0

            if temp1:
                val1 = temp1.val
                temp1 = temp1.next
            
            if temp2:
                val2 = temp2.val
                temp2 = temp2.next

            val_sum = val1 + val2 + carry
            temp3.next = ListNode(val_sum % 10)

            carry = val_sum // 10

            temp3 = temp3.next
        
        if carry:
            temp3.next = ListNode(carry)

        return res.next