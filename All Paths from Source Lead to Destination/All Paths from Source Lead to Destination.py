class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Standard DFS Approach:
        """
        def dfs(i):
            if len(graph[i]) == 0:
                return i == destination
            # Seen this node. Is a cycle.
            elif visited[i] == 1:
                return False
            # Processed this node before, which if hasn't returned False, means the path is good.
            elif visited[i] == 2:
                return True
            else:
                visited[i] = 1
                for j in graph[i]:
                    if not dfs(j):
                        return False
                visited[i] = 2
                return True
        
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
        visited = [0 for _ in range(n)]
        return dfs(source)
        """
        Modified Kahn's Algorithm Approach:
        Using Kahn's Algorithm from destination rather than source, we can traverse all paths at once.
        Instead of indegree though, we check outdegree.

        If we have any cycles we break rule 3.
        
        Time: O(V+E)
        Space: O(V+E)
        """
        """
        adj = { i : set() for i in range(n) }
        outdegree = [0] * n

        for out, to in edges:
            if out == destination: return False  # No outgoing edges from destination allowed

            adj[to].add(out)
            outdegree[out] += 1

        q = deque([destination])

        while q:
            node = q.popleft()

            if node == source:  # found path that led to destination
                return True
            
            for neighbor in adj[node]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    q.append(neighbor)

        return False
        """