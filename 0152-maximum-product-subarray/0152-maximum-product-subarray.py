class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # neetcode io dp
        res = max(nums)
        curMax, curMin = 1, 1  # keep track of min and max and do calculations by that

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)

        return res