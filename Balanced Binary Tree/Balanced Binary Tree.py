# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition:
        Find the depth of the two trees from the root node and return whether their depths
         are <= 1.
        """
        if not root:
            return True

        def longest_depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_depth = longest_depth(root.left) + 1
            right_depth = longest_depth(root.right) + 1

            return max(left_depth, right_depth)

        return longest_depth(root.left) - longest_depth(root.right) <= 1