class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(1)
        if len(nums) == 0:
            return 0

        last_increasing = last_decreasing = nums[0]
        increasing_streak = decreasing_streak = 1
        longest_monotonic = 1

        # O(n)
        for num in nums[1:]:
            if num > last_increasing:
                increasing_streak += 1
                longest_monotonic = max(longest_monotonic, increasing_streak)
            else:
                increasing_streak = 1

            if num < last_decreasing:
                decreasing_streak += 1
                longest_monotonic = max(longest_monotonic, decreasing_streak)
            else:
                decreasing_streak = 1

            last_increasing = num
            last_decreasing = num

        return longest_monotonic
