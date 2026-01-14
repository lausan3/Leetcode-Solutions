# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
        Top Down Memoization Solution:
        At any state of a full tree, a tree MUST have an odd number of nodes (odd root or odd root + even children).
        Therefore, we can construct a hashmap of odd numbers to the subtree at that level and reconstruct trees to return.
        """
        memo = {}  # i : [root nodes of all possible fbts with i nodes]

        if n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode()]
        elif n in memo:
            return memo[n]
        
        res = []
        
        for i in range(1, n - 1, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)
        
            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)
            
        memo[n] = res

        return res