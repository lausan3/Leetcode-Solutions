class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart, newEnd = newInterval
        n = len(intervals)
        i = 0

        # add all intervals before new interval
        while i < n and newStart > intervals[i][0]:
            res.append(intervals[i])
            i += 1

        # merge last interval if needed
        if not res or res[-1][1] < newStart:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], newEnd)

        while i < n:
            start, end = intervals[i]

            if res[-1][1] < start:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], end)
            
            i += 1

        return res