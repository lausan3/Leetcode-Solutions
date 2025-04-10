class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # O(n) Time and O(n) Space approach:
        # Init set operations
        # Add all nums > k to the set. If we come across a number < k, return -1.
        # Return length of set.

        operations_count = set()

        for num in nums:
            if num < k:
                return -1
            
            operations_count.add(num)
            
        return len(operations_count) - (1 if k in operations_count else 0)