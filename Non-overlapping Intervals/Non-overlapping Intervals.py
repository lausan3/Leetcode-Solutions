class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy solution (from editorial):

        Sort intervals by ending times
        Keeping track of the last end time we saw, compare the curr start time and last end time,
            if current interval doesn't overlap with last one, then keep track of this interval's end time
            else "remove" one interval bc they overlap

        # Time: O(n log n)
        # Space: O(n) bc sorting in Python
        """
        intervals.sort(key=lambda interval: interval[1])
        
        removed = 0
        last_end_time = -inf

        for start, end in intervals:
            if start >= last_end_time:  # current interval doesn't overlap, can keep it for free
                last_end_time = end
            else:  # overlaps, "remove" it
                removed += 1

        return removed