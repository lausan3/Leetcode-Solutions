# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        maximum = root.val
        maxLevel = currLevel = 1

        q = deque([root])

        while q:
            n = len(q)

            currSum = 0

            for i in range(n):
                curr = q.popleft()

                currSum += curr.val
                
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            
            if currSum > maximum:
                maximum = currSum
                maxLevel = currLevel

            currLevel += 1

        return maxLevel