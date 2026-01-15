class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        Time: O(n^2)
        Space: O(1)
        """
        min_distance = float('inf')
        n = len(nums)

        for i in range(n - 2):
            value_to_compare = nums[i]

            j = i + 1
            while j < n and nums[j] != value_to_compare:
                j += 1
            
            k = j + 1
            while k < n and nums[k] != value_to_compare:
                k += 1
            
            if (i < n and j < n and k < n and 
                i != j != k and 
                nums[i] == nums[j] == nums[k]):
                potential_min_dist = abs(i - j) + abs(j - k) + abs(k - i)
                min_distance = min(min_distance, potential_min_dist)
            
        return min_distance if min_distance < float('inf') else -1
            