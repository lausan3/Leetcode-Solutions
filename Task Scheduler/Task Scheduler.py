class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Greedy BFS Scheduling solution:

        In this solution, we want to be greedy by scheduling tasks that have the greatest amount left to process while also
         accounting for the n interval time constraint.

        We do this by using a max heap to find the task with the greatest count to schedule.

        Time: O(n) where n is the amount of tasks
        Space: O(26)
        """

        task_counts = Counter(tasks)
        # O(n)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        # as long as we have items in the maxHeap or the queue, then we have tasks to perform still
        while max_heap or q:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap) # reduce count by 1, don't forget count is negative
                if cnt:
                    q.append([cnt, time + n]) # time + n is next time this task can be processed

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0]) # push it back to the queue
        
        return time