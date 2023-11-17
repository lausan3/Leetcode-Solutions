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
        # bfs solution
        # q = collections.deque()
        # visited = {}
        # if node:
        #     visited[node] = Node(node.val)
        #     q.append(node)

        # while q:
        #     process = q[0]

        #     if process not in visited:
        #         visited[process] = Node(process.val)
            
        #     # process neighbors
        #     for neighbor in process.neighbors:
        #         if neighbor not in visited:
        #             q.append(neighbor)
        #             visited[neighbor] = Node(neighbor.val)
        #             visited[process].neighbors.append(neighbor)

        #     q.popleft()


        # return visited[node] if node else None



        # dfs solution
        nodeMap = {}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]

            # deep copy node
            copy = Node(node.val)
            nodeMap[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else None