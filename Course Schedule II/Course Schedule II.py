class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sort solution (BFS/Kahn's Algorithm)
        """
        adj = [ set() for _ in range(numCourses) ]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].add(course)
            indegree[course] += 1

        q = deque( [ i for i in range(numCourses) if indegree[i] == 0 ] )
        visited = set()

        while q:
            pre = q.popleft()

            if pre in visited:
                return []

            visited.add(pre)

            for course in adj[pre]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    q.append(course)

        return list(visited)