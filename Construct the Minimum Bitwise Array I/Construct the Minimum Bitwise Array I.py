class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        Brute Force Solution:
        1. For each i in nums, find a number from 0 -> nums[i] where 
           ans[i] | ans[i] + 1 == nums[i]

        Time: O(n * m) where m = max(nums)
        Space: O(n) or O(1) depending on if answer counted
        """
        n = len(nums)
        ans = [-1 for _ in range(n)]

        for i in range(n):
            for possible_or in range(nums[i]):
                if possible_or | possible_or + 1 == nums[i]:
                    ans[i] = possible_or
                    break

        return ans