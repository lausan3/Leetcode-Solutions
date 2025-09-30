class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Optimized solution from Marouane - Three sum with Two Pointer
        # Time: O(n^2). Space: O(log n)
        n = len(nums)
        count = 0

        nums.sort()

        # O(n^2)
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1

            while i < j:
                # Since the array is sorted, if the sum of the smallest and largest
                #  sides is greater than the last side, then all sides in the range
                #  will fulfil this as well.
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1

        return count

        # Brute force
        # Time: O(n^3). Space: O(1)
        # n = len(nums)
        # count = 0

        # # O(n^3)
        # for i in range(n - 2):
        #     for j in range(i + 1, n - 1):
        #         for k in range(j + 1, n):
        #             if (nums[i] + nums[j] > nums[k] and
        #                 nums[i] + nums[k] > nums[j] and
        #                 nums[j] + nums[k] > nums[i]):
        #                 count += 1

        # return count