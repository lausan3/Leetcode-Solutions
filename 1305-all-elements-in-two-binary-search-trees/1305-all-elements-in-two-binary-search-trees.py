# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def reverseInorderDFS(root, curr: List[int]) -> List[int]:
            if not root:
                return curr

            reverseInorderDFS(root.left, curr)
            curr.append(root.val)
            reverseInorderDFS(root.right, curr)

            return curr

        # populate a list for each tree
        root1Ascending = reverseInorderDFS(root1, [])
        root2Ascending = reverseInorderDFS(root2, [])
        
        if not root1Ascending:
            return root2Ascending
        elif not root2Ascending:
            return root1Ascending
            
        oneLen = len(root1Ascending)
        twoLen = len(root2Ascending)

        res = []

        l, r = 0, 0

        # merge
        while l < oneLen or r < twoLen:  
            if l >= oneLen:
                res.append(root2Ascending[r])
                r += 1
                continue
            elif r >= twoLen:
                res.append(root1Ascending[l])
                l += 1
                continue
                
            one, two = root1Ascending[l], root2Ascending[r]

            if one <= two:
                res.append(one)
                l += 1
            else:
                res.append(two)
                r += 1

        return res