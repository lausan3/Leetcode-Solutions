class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        This problem is solved by making sure we don't have cycles
         in the graph. Therefore, we use topological sort.

        BFS Topological Sort solution (Kahn's Algorithm):

            build adjacency list of prereqs to the courses they fulfill
            init queue with every node that has an indegree of 0
            init visited set
            while queue is nonempty, process node n
                if we've seen node n, return false
                else, add it to the set

                remove all edges outgoing from node n
                if a node that got its incoming edge from n removed has
                 no more incoming edges, append it to the queue

            return true

        Time: O(V + E)
        Space: O(V)
        """
        # adj_list = { i : set() for i in range(numCourses) }
        # indegrees = [0] * numCourses

        # # build adjacency list
        # for course, prereq in prerequisites:
        #     adj_list[prereq].add(course)
        #     indegrees[course] += 1

        # visit_count = 0
        # q = deque()

        # # add initial 0 indegrees
        # q.extend([i for i in range(numCourses) if indegrees[i] == 0])

        # # This is Kahn's algorithm
        # while q:
        #     prereq = q.popleft()
        #     visit_count += 1
            
        #     courses = adj_list[prereq]
            
        #     for course in courses:
        #         indegrees[course] -= 1

        #         if indegrees[course] == 0:
        #             q.append(course)

        # return visit_count == numCourses

        """
        The DFS version of topological sort involves going through courses and their prereqs
         until we have gone through all courses. If at any moment we have seen a prereq before,
         we have a cycle.

        Note that the adjacency list differs from the BFS solution because we are building a list
         of courses to their prereqs instead of prereqs to their courses.

        DFS Topological Sort Solution:

            init adjacency list of courses to their prerequisites
            init visited set

            for every course, DFS
                if we've seen the course before, we have a cycle. Return false

                add the course to visited

                for every prereq, dfs into it

                reset state by removing the course from visited
        """
        adj_list = { i : [] for i in range(numCourses)}  # course number : prerequesites

        for course, prereqs in prerequisites:
            adj_list[course].append(prereqs)

        # visit set to detect cycles.
        # if a prerequisite is in the set, then it's a loop.
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            
            visited.add(course)

            for pre in adj_list[course]:
                if not dfs(pre): return False

            visited.remove(course)
            # adj_list[course] = []   # visited all course prereqs, so reset the prereqs list
            return True

        for course in range(numCourses):
            if not dfs(course): return False

        return True