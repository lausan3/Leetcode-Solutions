class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # O(n) idea:
        # create an auxillary array where each element is the running count of its number
        # construct largest array where bounds are at k.
        # return length of this array

        # Time: O(n), Space: O(n)

        aux = []
        count = {}

        for num in nums:
            running_count = count.get(num, 0) + 1
            count[num] = running_count
            aux.append(running_count)

        l = r = 0
        largest_subarray = 1
        while r < len(nums):
            if aux[r] > k:
                largest_subarray = max(largest_subarray, r - l)

                l = r

            r += 1

        return largest_subarray
