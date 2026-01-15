"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Intuition:
        For these types of node deep copying problems, as long as we keep a hashmap
        of original node to copied node, we should be fine.

        Time: O(n)
        Space: O(n)
        """
        old_to_copy_nodes = {None : None}

        temp = head
        while temp:
            copy = Node(temp.val)
            old_to_copy_nodes[temp] = copy
            temp = temp.next
        
        temp = head
        while temp:
            copy = old_to_copy_nodes[temp]
            copy.next = old_to_copy_nodes[temp.next]
            copy.random = old_to_copy_nodes[temp.random]
            temp = temp.next

        return old_to_copy_nodes[head]