class MyCalendarThree:

    """
    |---- 1 --- 2 ----- -1 ----- 1  ---- 0 --- -1 ---- 1 ----- 0 ----- -1 ---- |
    |---- 5 --- 10 ---- 15 ---- 20 ---- 25 --- 40 ---- 50 ---- 55 ---- 60 ---- |
    """
    def __init__(self):
        self.bookings = sortedcontainers.SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.bookings[startTime] = self.bookings.get(startTime, 0) + 1
        self.bookings[endTime] = self.bookings.get(endTime, 0) - 1

        pre_sum = 0
        max_k = 0

        for freq in self.bookings.values():
            pre_sum += freq

            max_k = max(max_k, pre_sum)

        return max_k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)