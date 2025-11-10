class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Brute force approach:

            Sort the list by weight,
            maintain a pointer at the start and end,
                if their sum is <= limit, adjust both pointers
                else append the larger weight

        Time: O(n log n)
        Space: O(log n), maximum n / 2 boats
        """
        boats = []

        l, r = 0, len(people) - 1
        weights = sorted(people)

        while l <= r:
            left, right = weights[l], weights[r]

            if left + right <= limit:
                boats.append(limit - left - right)
                l += 1
                r -= 1
            elif left > right:
                boats.append(limit - left)
                l += 1
            else:
                boats.append(limit - right)
                r -= 1

        return len(boats)
