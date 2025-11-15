class Solution:
    """
    Brute force O(n):

    Linearly search for the place to insert the interval
        1. Insert intervals where not not overlapped
        2. Insert new intervals and fix overlaps
        3. Insert remaining intervals

    Time: O(n)          l
    Space: O(n)
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        new_start, new_end = newInterval
        i = 0

        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1

        while i < n and max(intervals[i][0], new_start) <= min(intervals[i][1], new_end):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
