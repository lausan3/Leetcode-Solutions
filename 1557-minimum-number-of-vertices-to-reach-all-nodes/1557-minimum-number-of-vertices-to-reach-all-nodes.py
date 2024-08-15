class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # O(n)
        unreachableNodes = set([i for i in range(n)])

        for _, incomingNode in edges:
            if incomingNode in unreachableNodes:
                unreachableNodes.remove(incomingNode)

        return list(unreachableNodes)