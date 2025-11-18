class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        My attempt at a primitive union find algorithm:
        """
        N_MAX = 2001
        roots = [N_MAX for _ in range(n)]
        in_adj = [set() for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for start, end in edges:
            in_adj[end].add(start)
            indegree[end] += 1

        # for every node that doesn't have incoming edges, 
        for node, ins in enumerate(indegree):
            if ins == 0:
                roots[node] = node

        # union find
        for i in range(n):
            if roots[i] != N_MAX:
                continue
            
            for adj in in_adj[i]:
                roots[i] = min(roots[i], roots[adj])

        return len(list(set(roots)))  # return length of list of all unique values