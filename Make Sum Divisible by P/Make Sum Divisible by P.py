class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # calculate initial sum
        # init map indexSubarrayToSum. key: index, val: sum if nums[index] 
        ## was removed along with the nums after it
        # loop from 0 -> len(nums) (amount of numbers we remove from a point)
        #   loop through indicies, if any are evenly divisible by p, return i
        #   calculate indexSubarrayToSum[i] - nums[i]
        # return -1 if we reach the end

        # Time: O(n^2), Space: O(n)

        initial_sum = sum(nums)
        index_subarray_to_sum = {}

        for i in range(len(nums)):
            index_subarray_to_sum[i] = initial_sum

        for i in range(len(nums)):
            print(index_subarray_to_sum)
            for j, prefix_sum in index_subarray_to_sum.items():
                if prefix_sum % p == 0:
                    return i
                
                if i + j < len(nums):
                    index_subarray_to_sum[j] = prefix_sum - nums[i + j]

        return -1