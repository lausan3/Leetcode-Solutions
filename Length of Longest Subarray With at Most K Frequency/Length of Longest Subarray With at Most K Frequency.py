class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # O(n) idea:
        # create an auxillary array where each element is the running count of its number
        # construct largest array where bounds are at k.
        # return length of this array
        # Note: Right idea, but doesn't take into account the actual frequencies of the numbers.

        # Time: O(n), Space: O(n)

        longest_subarray, l = 0, -1
        freq = Counter()

        for r, num in enumerate(nums):
            freq[num] += 1
            
            while freq[num] > k:
                l += 1
                freq[nums[l]] -= 1
            
            longest_subarray = max(longest_subarray, r - l)

        return longest_subarray


