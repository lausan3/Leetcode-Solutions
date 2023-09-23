# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            # append the right-most node's value
            if q[-1]:
                res.append(q[-1].val)

            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()

                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
        return res