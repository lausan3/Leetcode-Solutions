class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Optimized Tabulation DP Approach:

        Start at the bottom (amount of money we can get from robbing the last house, 
         aka rob_next). Then work your way up using a recurrence relation of
         rob(i + 2) + nums[i] (robbing from second-to-last house) 
         and rob(i + 1) (robbing this house)

        Time: O(n)
        Space: O(1)
        """
        # if not nums:
        #     return 0

        # n = len(nums)
        # rob_next_plus_one, rob_next = 0, nums[n - 1]

        # for i in range(n - 2, -1, -1):
        #     temp = max(rob_next_plus_one + nums[i], rob_next)

        #     rob_next_plus_one = rob_next
        #     rob_next = temp

        # return rob_next
        """
        Top-Down Memoized Approach:

        If we were using recursion, we should try to rob a house, or skip a house and 
        rob that one.
        This can be inefficient, unless we store the result in a memo table.

        Time: O(n)
        Space: O(n)
        """
        n = len(nums)
        memo = {}

        def rob(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            rob_this = nums[i] + rob(i + 2)
            rob_next = rob(i + 1)

            memo[i] = max(rob_this, rob_next)

            return memo[i]

        return rob(0)
