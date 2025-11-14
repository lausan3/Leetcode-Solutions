class MyCalendarTwo:
    """
    Using line-sweep technique, we can effectively calculate any double bookings and extend it if needed.

    Essentially, the line-sweep technique involves keeping a number line of starts (+1) and ends (-1),
        then performing a prefix sum over the number line to see the number of overlaps.

    Time: O(n)
    Space: O(n)
    """

    def __init__(self):
        self.bookings = sortedcontainers.SortedDict()
        self.max_overlaps = 2

    # O(n) where n = len(bookings)
    def book(self, startTime: int, endTime: int) -> bool:
        self.bookings[startTime] = self.bookings.get(startTime, 0) + 1
        self.bookings[endTime] = self.bookings.get(endTime, 0) - 1

        overlaps = 0

        for count in self.bookings.values():
            overlaps += count  # prefix sum

            if overlaps > self.max_overlaps:
                # rollback
                self.bookings[startTime] -= 1
                self.bookings[endTime] += 1

                if self.bookings[startTime] == 0:
                    del self.bookings[startTime]

                return False

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)