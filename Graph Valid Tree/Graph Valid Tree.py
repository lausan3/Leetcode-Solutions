class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        indegree = [0] * n

        for _, end in edges:
            indegree[end] += 1

            if indegree[end] > 1:
                return False

        return sum(indegree) == n - 1