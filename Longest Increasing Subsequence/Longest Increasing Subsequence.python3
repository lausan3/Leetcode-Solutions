class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        longest_subseq = 0
    
        for i, num in enumerate(nums):
            longest_possible_subseq = 1
            
            for j, longest_at_j in cache.items():
                if num > nums[j]:
                    longest_possible_subseq = max(longest_possible_subseq, longest_at_j + 1)
                    
            cache[i] = longest_possible_subseq

            longest_subseq = max(longest_subseq, longest_possible_subseq)
        
        return longest_subseq