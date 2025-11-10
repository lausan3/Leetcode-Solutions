class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Brute force solution:

            init min_height and set to track roots with this height

            for every node 0 -> n - 1,
                apply dfs or bfs to find height of tree
                keep track of the root value and its height, only keeping minimums
        
        Time: O(V * V + E)

        Note: This WOULD work if there wasn't a time constraint.
        """
        # graph = { i : set() for i in range(n) }

        # # populate graph/adjacency list
        # # O(E)
        # for a, b in edges:
        #     graph[a].add(b)
        #     graph[b].add(a)

        # # O(V)
        # def determine_height(rooted_at_node: int) -> int:
        #     q = deque([ (rooted_at_node, 0) ]) # node value, height
        #     max_height_seen = 0
        #     visited = set()

        #     while q:
        #         node, height = q.popleft()

        #         visited.add(node)
        #         max_height_seen = max(max_height_seen, height)

        #         for adj in graph[node]:
        #             if adj in visited:
        #                 continue

        #             q.append( (adj, height + 1) )

        #     return max_height_seen

        # min_height = float("inf")
        # roots_with_min = []

        # # O(V)
        # for root in range(n):
        #     # O(V)
        #     height = determine_height(root)

        #     if height < min_height:
        #         min_height = height
        #         roots_with_min = [root]
        #     elif height == min_height:
        #         roots_with_min.append(root)

        # return roots_with_min

        """
        Optimal Topological Sort Approach (from editorial):

        Essentially, we can imagine each tree/graph as a circle. We can minimize the height of the
         graph by finding the centroid of this circle using a modified version of topo sort.
        """
        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves