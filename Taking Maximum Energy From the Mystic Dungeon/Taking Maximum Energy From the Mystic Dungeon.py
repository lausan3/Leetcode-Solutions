class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # O(log n) binary search solution
        n = len(heights)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            # peak is after middle - search right half
            if heights[m] < heights[m + 1]:
                l = m + 1
            # peak is before middle - search left half
            else:
                r = m

        return l