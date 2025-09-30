class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Brute Force
        # Time: O(n^2). Space: O(n^2).
        # n = len(nums)

        # if n == 1:
        #     return nums[0]

        # newNums = [0] * (n - 1)

        # # O(n)
        # for i in range(n - 1):
        #     newNums[i] = (nums[i] + nums[i+1]) % 10

        # return self.triangularSum(newNums)

        # Optimized in-place
        # Time: O(n). Space: O(1)
        # O(n)
        n = len(nums)
        newNums = nums

        for i in range(n):
            for j in range(n - i - 1):
                newNums[j] = (nums[j] + nums[j+1]) % 10

        return newNums[0]