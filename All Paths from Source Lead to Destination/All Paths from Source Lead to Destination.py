class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = { i : set() for i in range(n) }

        for out, to in edges:
            adj[out].add(to)

        visited = set()

        def dfs(cur: int):
            if len(adj[cur]) == 0:
                return cur == destination

            if cur in visited:
                return False
            
            visited.add(cur)

            for new in adj[cur]:
                if not dfs(new):
                    return False

            visited.remove(cur)

            return True

        return dfs(source)