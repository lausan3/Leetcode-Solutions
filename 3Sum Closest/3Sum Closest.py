class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff_sum = float('inf')
        min_diff = float('inf')
        n = len(nums)
        nums.sort()

        # first num
        for i in range(n):
            l, r = i + 1, n - 1

            while l < r:
                proposed_sum = nums[i] + nums[l] + nums[r]
                abs_diff = abs(target - proposed_sum)

                if abs_diff < min_diff:
                    min_diff_sum = proposed_sum
                    min_diff = abs_diff

                if proposed_sum < target:
                    l += 1
                else:
                    r -= 1

            if min_diff_sum == target:
                break
                
        return min_diff_sum