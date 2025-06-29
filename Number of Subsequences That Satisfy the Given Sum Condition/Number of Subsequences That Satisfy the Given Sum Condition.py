class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)

        # O(n log n)
        nums.sort()

        powers = [1] * n

        for i in range(1, n):
            powers[i] = powers[i - 1] * 2

        l, r = 0, n - 1
        count = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                count += powers[r - l]
                l += 1
            else:
                r -= 1
        
        return count % mod