class MyCalendarTwo:

    def __init__(self):
        self.bookings = []  # all bookings
        self.overlaps = []  # double overlaps

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.overlaps:
            if self.does_overlap(start, end, startTime, endTime):
                return False

        for start, end in self.bookings:
            if self.does_overlap(start, end, startTime, endTime):
                self.overlaps.append(self.get_overlap(start, end, startTime, endTime))

        self.bookings.append((startTime, endTime))
        return True

    def does_overlap(self, start1, end1, start2, end2) -> bool:
        return max(start1, start2) < min(end1, end2)

    def get_overlap(self, start1, end1, start2, end2) -> tuple:
        return (max(start1, start2), min(end1, end2))

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)