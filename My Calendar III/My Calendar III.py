"""
O(N log C) Segment Tree Solution:

A Segment tree is a binary tree where each node includes a part of the imaginary number line from 0 -> C (largest time possible).
 We can also attach any values we want on top of this like minimums, maximums, ect. Which makes searching O(log C).

Time: O(N log C) where C is the largest time in the bookings.
Space: O(N log C)
"""
class MyCalendarThree:
    
    def __init__(self):
        self.vals = Counter()  # map of the max number of events included in the range L, R.
        self.lazy = Counter()  # map of the number of events covering all times in the range.
        
    def book(self, startTime: int, endTime: int) -> int:
        self.update(startTime, endTime - 1)
        return self.vals[1]

    def update(self, start: int, end: int, left: int = 0, right: int = 10**9, i: int = 1) -> None:
        if start > right or end < left:  # this node's range doesn't overlap with interval
            return

        if start <= left <= right <= end:  # this node's entire range overlaps with interval
            self.vals[i] += 1
            self.lazy[i] += 1
        else:  # this node's range doesn't fully cover the interval, binary search left and right halves
            mid = (left + right) // 2
            self.update(start, end, left, mid, i * 2)  # explore left
            self.update(start, end, mid + 1, right, i * 2 + 1)  # explore right

            # this is the same as taking vals from above since we modify them.
            self.vals[i] = self.lazy[i] + max(self.vals[2 * i], self.vals[2 * i + 1])

"""
O(N^2) Line Sweep Technique:

Time: O(N^2)
Space: O(N)
"""
# class MyCalendarThree:

#     def __init__(self):
#         self.bookings = sortedcontainers.SortedDict()

#     def book(self, startTime: int, endTime: int) -> int:
#         self.bookings[startTime] = self.bookings.get(startTime, 0) + 1
#         self.bookings[endTime] = self.bookings.get(endTime, 0) - 1

#         pre_sum = 0
#         max_k = 0

#         for freq in self.bookings.values():
#             pre_sum += freq

#             max_k = max(max_k, pre_sum)

#         return max_k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)