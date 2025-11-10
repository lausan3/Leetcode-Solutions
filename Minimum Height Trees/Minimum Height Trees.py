class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Brute force solution:

            init min_height and set to track roots with this height

            for every node 0 -> n - 1,
                apply dfs or bfs to find height of tree
                keep track of the root value and its height, only keeping minimums
        
        Time: O(V * V + E)
        """
        graph = { i : set() for i in range(n) }

        # populate graph/adjacency list
        # O(E)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # O(V)
        def determine_height(rooted_at_node: int) -> int:
            q = deque([ (rooted_at_node, 0) ]) # node value, height
            max_height_seen = 0
            visited = set()

            visited.add(rooted_at_node)
            while q:
                node, height = q.popleft()

                visited.add(node)
                max_height_seen = max(max_height_seen, height)

                for adj in graph[node]:
                    if adj in visited:
                        continue
                    visited.add(adj)
                    q.append( (adj, height + 1) )

            return max_height_seen

        min_height = float("inf")
        roots_with_min = []

        # O(V)
        for root in range(n):
            # O(V)
            height = determine_height(root)

            if height < min_height:
                min_height = height
                roots_with_min = [root]
            elif height == min_height:
                roots_with_min.append(root)

        return roots_with_min