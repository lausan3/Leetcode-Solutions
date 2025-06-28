class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # greedy O(n log n) solution
        
        index_to_num = zip(
            [i for i in range(len(nums))], nums
        )

        # sort by values
        largest_k_nums = sorted(index_to_num, key=lambda x: x[1], reverse=True)[:k]

        # sort by indices
        sorted_by_indices = sorted(largest_k_nums)

        res = [num for _, num in sorted_by_indices]

        return res