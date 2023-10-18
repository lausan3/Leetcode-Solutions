class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task is 1 unit of time
        # minimize idle time

        # python Counter() is a hashmap of counts of objects. in this case, it counts each task and its occurances
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        # as long as we have items in the maxHeap or the queue, then we have tasks to perform still
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: # if count is non-zero
                    q.append([cnt, time + n]) # time + n is next time this task can be processed

            if q and q[0][1] == time: # see if the task at the front of the queue is ready to be reproccessed
                heapq.heappush(maxHeap, q.popleft()[0]) # push it back to the queue
        
        return time