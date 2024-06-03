# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        iToNode = {}
        temp = head
        n = 0

        # traverse list and count the maount of nodes, while also saving them into a hashmap
        while temp != None:
            iToNode[n] = ListNode(temp.val)
            n += 1
            temp = temp.next

        temp = head

        # arrange nodes
        for i in range(0, n // 2):
            if temp and n - i - 1 in iToNode:
                temp.next = iToNode[n - i - 1]
                temp = temp.next
            if temp and i + 1 in iToNode:
                temp.next = iToNode[i + 1]
                temp = temp.next

        temp.next = None