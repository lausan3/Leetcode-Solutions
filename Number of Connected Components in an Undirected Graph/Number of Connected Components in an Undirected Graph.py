class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Union Find Solution:

        Time: O(V + E)
        Space: O(V)
        """
        root = [i for i in range(n)]

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            
            return root[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                root[rx] = ry

        for x, y in edges:
            union(x, y)

        unique_roots = set([find(i) for i in range(n)])
        
        return len(unique_roots)
        """
        Simple DFS Solution:

        init adj list

        init visited set
        init connected components counter

        for each node
            if node not visited
                increment counter

                add node to visited

                visit each neighbor

        Time: O(V + E)
        Space: O(V + E]
        """
        # adj = [set() for _ in range(n)]

        # for start, end in edges:
        #     adj[start].add(end)
        #     adj[end].add(start)

        # visited = set()
        # counter = 0

        # def dfs(i: int) -> None:
        #     visited.add(i)

        #     for neighbor in adj[i]:
        #         if neighbor not in visited:
        #             dfs(neighbor)

        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)

        #         counter += 1

        # return counter
