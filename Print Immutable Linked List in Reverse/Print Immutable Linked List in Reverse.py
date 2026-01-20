# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """
        Recursive Solution:
        Start a recursive chain, printing when we return to print in reverse.

        Time: O(n)
        Space: O(n)
        """
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
        """
        Iterative Linear BF solution:
        1. Go through the linked list, keeping track of the order in a list.
        2. Go through the list in reverse and print each one.
        
        Time: O(n)
        Space: O(n)
        """
        # order = []
        
        # temp = head
        # while temp:
        #     order.append(temp)
            
        #     temp = temp.getNext()
            
        # for node in reversed(order):
        #     node.printValue()