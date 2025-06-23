# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            next_odd = odd.next.next
            next_even = even.next.next

            odd.next = next_odd
            even.next = next_even
            
            odd = next_odd
            even = next_even

        odd.next = even_head

        return head