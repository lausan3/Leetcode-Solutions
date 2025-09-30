class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Optimized in-place
        # Time: O(n^2). Space: O(1) optimized
        n = len(nums)

        # O(n^2)
        for i in range(n):
            for j in range(n - i - 1):
                nums[j] = (nums[j] + nums[j+1]) % 10

        return nums[0]

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