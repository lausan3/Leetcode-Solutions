class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        q = deque([0])
        seen = set([0])

        while q:
            node = q.popleft()

            for neighbor in adj[node]:
                if neighbor in seen:
                    continue

                seen.add(neighbor)
                q.append(neighbor)

        return len(seen) == n
