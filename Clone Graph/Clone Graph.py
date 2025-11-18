"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        visited = {}

        visited[node] = Node(node.val, [])

        q = deque([node])

        while q:
            curr = q.popleft()

            for next_node in curr.neighbors:
                if next_node not in visited:
                    visited[next_node] = Node(next_node.val, [])
                    q.append(next_node)

                visited[curr].neighbors.append(visited[next_node])

        return visited[node]
