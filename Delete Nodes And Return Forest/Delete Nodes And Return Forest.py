# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        root = self.dfs(root, to_delete_set, forest)

        if root:
            forest.append(root)
        
        return forest

    def dfs(self, node: Optional[TreeNode], to_delete: Set[int], forest: List[TreeNode]):
        if not node:
            return None
        
        node.left = self.dfs(node.left, to_delete, forest)
        node.right = self.dfs(node.right, to_delete, forest)

        # delete by returning null, meaning node.left and node.right would be 
        #  null as well if they had to be deleted.
        if node.val in to_delete:
            if node.left:
                forest.append(node.left)
            
            if node.right:
                forest.append(node.right)

            return None
        
        return node