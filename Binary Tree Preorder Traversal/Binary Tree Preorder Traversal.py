# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []

        if not root:
            return preorder

        preorder.append(root.val)
        
        preorder.extend(self.preorderTraversal(root.left))
        preorder.extend(self.preorderTraversal(root.right))

        return preorder