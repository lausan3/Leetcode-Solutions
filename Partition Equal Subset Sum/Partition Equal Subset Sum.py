class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # # Brute force: O(2^n) time (subsets). O(2^n) space
        # # This solution is too slow for LeetCode.
        # n = len(nums)

        # # Approach:
        # #  Use backtracking algorithm that finds all subsets
        # #    for both subsets, if their sum is equal, return true.
        # #  If we can't find two equal subset sums, return false.

        # def FindEqualSubsetSum(i: int, sub1: int, sub2: int) -> bool:
        #     if i >= n:
        #         return sub1 == sub2

        #     num = nums[i]

        #     # First choice: Add num to sub1
        #     found_equal_sum_1 = FindEqualSubsetSum(i + 1, sub1 + num, sub2)

        #     # Second choice: Add num to sub2
        #     found_equal_sum_2 = FindEqualSubsetSum(i + 1, sub1, sub2 + num)
            
        #     return found_equal_sum_1 or found_equal_sum_2

        # return FindEqualSubsetSum(0, 0, 0)

        # Approach 2: Dynamic Programming
        # Got this idea from user Sung Jinwoo on LC.

        # Idea: Since both subsets need to be equal, the sum of the entire array needs to be even
        #  or else we can't divide the subset in two equal halves.

        # Furthermore, we can bound the solution space to O(n * m). where m is the total sum of the array.
        # Time: O(n * m). Space: O(m).
        
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        # have_sum[i] represents whether we can create a subset of nums that equals i.
        have_sum = [False] * (target_sum + 1)
        have_sum[0] = True  # We can always get a sum of 0 by omitting every value.


        for num in nums:
            # Perform in reverse to not count the same number twice since we're going from the nearest
            #  subset sum from subs_sum to subs_sum itself.
            # If we did it in left -> right order, we could have an issue where "num" is counted from
            #  one sum to another.
            # For example, if num = 1, then if subs_sum[1] == true, then subs_sum[2 - 1] would also be true.
            for subs_sum in range(target_sum, num - 1, -1):
                have_sum[subs_sum] = have_sum[subs_sum] or have_sum[subs_sum - num]

        return have_sum[target_sum]
            