class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Intuitive solution:

        First, sort intervals by start
        init count = 0
        for each pair of intervals i and i + 1, if they are overlapping, remove them and increment count

        # Time: O(n log n) or O(n^2) bc of pop
        # Space: O(n) bc sorting in Python
        """
        intervals.sort()

        removed = 0
        i = 0

        while i + 1 < len(intervals):
            curr, next = intervals[i], intervals[i + 1]

            if max(curr[0], next[0]) < min(curr[1], next[1]):
                intervals.pop(i + 1)
                removed += 1
            else:
                i += 1
            
        return removed