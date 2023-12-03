class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # neetcode io solution
        # we're going to use an adjacency list to compute the graph

        # adjacency list
        preMap = { i:[] for i in range(numCourses)}  # course number : prerequesites

        for course, prereqs in prerequisites:
            preMap[course].append(prereqs)

        # visit set to detect cycles.
        # if a prerequesite is in the set, then it's a loop.
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True
            
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False

            visit.remove(course)
            preMap[course] = []   # visited all course prereqs
            return True

        for course in range(numCourses):
            if not dfs(course): return False

        return True