class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        In this problem, we want to separate the stones array into two subarrays
         where each pair of X[i] and Y[j] are have as small of a difference as possible.

        We can achieve this using a Subset Sum Dynamic Programming solution in which
         we incrementally create an array representing the possible sums we can create
         by including the numbers in num.

        Time: O(n * s) where n is the number of stones and a is the sum of the stones.
        Space: O(s)
        """
        total = sum(stones)
        target = total // 2
        possible = [False] * (target + 1)
        possible[0] = True

        # for each stone, add it to a subset sum by ORing it with the possibility of
        #  a previous subset with this num.
        for num in stones:
            for s in range(target, num - 1, -1):
                possible[s] |= possible[s - num]

        # find largest subset sum that's possible and return its difference with the total.
        for s in range(target, -1, -1):
            if possible[s]:
                return total - 2 * s  # calculate difference

        """
        There's also the brute force recursive solution where you just calculate the
         minimum difference of each single possible subset.

        Time: O(2^n). Space: O(2^n) 
        """
        # total = sum(stones)
        # n = len(stones)

        # def dfs(i: int, x_total: int) -> int:
        #     if i == n:
        #         return abs(total - 2 * x_total) # return diff of two subsets

        #     add = dfs(i + 1, x_total + stones[i])
        #     dont_add = dfs(i + 1, x_total)

        #     return min(add, dont_add)

        # return dfs(0, 0)