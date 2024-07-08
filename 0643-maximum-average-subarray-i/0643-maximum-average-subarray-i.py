class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # O(n)
        l = 1
        windowSum = sum(nums[0:k])
        maxAvg = windowSum / k

        for r in range(k + 1, len(nums) + 1):
            windowSum += nums[r - 1] - nums[l - 1]

            maxAvg = max(maxAvg, windowSum / k)

            l += 1

        return maxAvg