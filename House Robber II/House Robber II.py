class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Intuitive Recursive Memoized Solution:

        Same as House Robber 1, except we compare two paths. Robbing from house[0]
         -> house[n-2], or robbing from house[1] -> house[n-1]

        Time: O(n)
        Space: O(n)
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob(i, max_i):
            if i > max_i:
                return 0

            if i in memo:
                return memo[i]

            rob_this = nums[i] + rob(i + 2, max_i)
            rob_next = rob(i + 1, max_i)

            memo[i] = max(rob_this, rob_next)
            return memo[i]

        memo = {}

        rob_from_house_1 = rob(0, n - 2)

        memo = {}

        rob_from_house_2 = rob(1, n - 1)

        return max(rob_from_house_1, rob_from_house_2)

        """
        Optimized Tabulation DP Approach:

        Start at the bottom (amount of money we can get from robbing the last house,
         aka rob_next). Then work your way up using a recurrence relation of
         rob(i + 2) + nums[i] (robbing from second-to-last house)
         and rob(i + 1) (robbing this house)

        Time: O(n)
        Space: O(1)
        """
        # def helper(arr):
        #     rob_next_plus_one, rob_next = 0, 0

        #     for num in arr:
        #         temp = max(rob_next_plus_one + num, rob_next)

        #         rob_next_plus_one = rob_next
        #         rob_next = temp

        #     return rob_next

        # return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
