class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Brute force approach:

            Sort the list by weight,
            maintain a pointer at the start and end,
                if their sum is <= limit, adjust both pointers
                else append the larger weight

        Time: O(n log n)
        Space: O(n), sort takes O(n) space in python
        """
        boats = 0

        l, r = 0, len(people) - 1
        weights = sorted(people)

        while l <= r:
            left, right = weights[l], weights[r]

            if left + right <= limit:
                l += 1
                r -= 1
            elif left > right:
                l += 1
            else:
                r -= 1

            boats += 1

        return boats
