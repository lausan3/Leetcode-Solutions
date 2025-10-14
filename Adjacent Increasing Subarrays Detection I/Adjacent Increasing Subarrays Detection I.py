class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # Editorial O(n) solution
        n = len(nums)

        count, prev_count = 1, 0
        longest_increasing_subarray = 0
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                prev_count, count = count, 1
            
            # is curr or prev count larger than current max?
            longest_increasing_subarray = max(longest_increasing_subarray, min(prev_count, count))
            # is the count of one subarray greater than current max?
            longest_increasing_subarray = max(longest_increasing_subarray, count // 2)
        
        return longest_increasing_subarray >= k