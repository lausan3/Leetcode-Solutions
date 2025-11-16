class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Line Sweep Solution:

        Same as Meeting Rooms I, but return the maximum amt of overlaps

        Time: O(n log n)
        Space: O(n)
        """
        meetings = sortedcontainers.SortedDict()

        for start, end in intervals:
            meetings[start] = meetings.get(start, 0) + 1
            meetings[end] = meetings.get(end, 0) - 1

        overlaps = 0
        min_rooms = 0
        for count in meetings.values():
            overlaps += count

            if overlaps > min_rooms:
                min_rooms = overlaps
            
        return min_rooms
