class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ### brute force is way too slow, O(n^3) to check all subarrays
        ### Optimal O(n) Time, O(n) space solution using hashmaps and cumulative sums
        count = s = 0  # s for sum
        hmap = { 0: 1 }  # sum[i] : count of sum[i]

        for i in range(len(nums)):
            s += nums[i]
            count += hmap.get(s - k, 0)

            hmap[s] = hmap.get(s, 0) + 1

        return count

        
        ### Intuitive O(n^2) start - end solution. O(1) Space
        # n = len(nums)
        # count = 0
        
        # for start in range(n):
        #     cum_sum = 0
        #     for end in range(start, n):
        #         cum_sum += nums[end]
        #         if cum_sum == k:
        #             count += 1

        # return count

        ### Cool cumulative sum array solution - O(n^2) time. O(n) space
        # n = len(nums)
        # sums = [0] * (n + 1)
        # count = 0

        # # populate sums
        # for i in range(1, n + 1):
        #     sums[i] = sums[i - 1] + nums[i - 1]

        # for start in range(n):
        #     for end in range(start + 1, n + 1):
        #         if sums[end] - sums[start] == k:
        #             count += 1
        
        # return count