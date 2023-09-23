# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # the LCA is the node that is the split or equal to one of the nodes. i.e., in the first example, 2 is
        # less than the root 6 and 8 is greater than the root so we return 6

        # time complexity: O(logn), space complexity: o(1)

        cur = root

        while cur:
            # traverse right if both values are greater than root
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # traverse left if both values are less than root
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # otherwise, we've found either one of the values is not consistent with the other or is equal to the root.
            else:
                return cur