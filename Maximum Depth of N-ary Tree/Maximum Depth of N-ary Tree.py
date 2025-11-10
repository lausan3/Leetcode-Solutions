"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q = deque([ (root, 1) ]) # node value, height
        max_height_seen = 0

        while q:
            node, height = q.popleft()

            max_height_seen = max(max_height_seen, height)

            for adj in node.children:
                q.append( (adj, height + 1) )

        return max_height_seen