class MyCalendar:

    def __init__(self):
        self.bookings = sortedcontainers.SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        i = self.bookings.bisect((startTime, endTime))

        if (
            (i > 0 and self.bookings[i - 1][1] > startTime) or  # if not at beginning and booking end time overlaps with start time
            (i < len(self.bookings) and self.bookings[i][0] < endTime)  # same in reverse
        ):
            return False

        self.bookings.add((startTime, endTime))

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)