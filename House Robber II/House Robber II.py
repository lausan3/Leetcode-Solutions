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
        def helper(arr):
            rob_next_plus_one, rob_next = 0, 0

            for num in arr:
                temp = max(rob_next_plus_one + num, rob_next)

                rob_next_plus_one = rob_next
                rob_next = temp

            return rob_next

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
