class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Brute force approach:

        Maintain a sorted list and use binary search to find update points.

        Time: O(n log n)
        Space: O(n)
        """
        boats = SortedList()

        # O(n)
        for weight in people:
            # O(log n)
            i = boats.bisect_left(weight)

            if i >= len(boats):
                # O(log n)
                boats.add(limit - weight)
            else:
                # O(log n)
                old_weight = boats.pop(i)
                # O(log n)
                boats.add(old_weight - weight)

        return len(boats)
