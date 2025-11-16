class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Line sweep algorithm solution:
        
        Construct imaginary number line of overlapping intervals
        Maintain rolling sum along number line,
            if sum is ever > 1, then person cannot attend all meetings

        Time: O(n log n)
        Space: O(n) for the interval counts map
        """
        overlaps = sortedcontainers.SortedDict()

        for start, end in intervals:
            overlaps[start] = overlaps.get(start, 0) + 1
            overlaps[end] = overlaps.get(end, 0) - 1

        overlap_amt = 0

        for count in overlaps.values():
            overlap_amt += count

            if overlap_amt > 1:
                return False

        return True