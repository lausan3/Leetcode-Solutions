class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Brute Force: O(n^2) Time, O(n) Space
        # Init operations count to 0
        # While we have numbers in the array,
        #   See if we have any duplicates
        #       return operations count if false
        #   if true, remove the first 3 numbers from arr if possible
        # Return operations count

        ops_count = 0

        while nums:
            seen_nums = set()
            distinct_array = True

            for num in nums:
                if num in seen_nums:
                    distinct_array = False
                    break
                
                seen_nums.add(num)

            if distinct_array:
                return ops_count
            
            ops_count += 1
            if len(nums) > 3:
                nums = nums[3:]
            else:
                nums = []
            
        return ops_count

        # More optimized approach: O(n) Time, O(n) Space
        # Init seen numbers to empty set
        # Loop through the array in reverse,
        #    if we've seen the number before, return index / 3
        #    Keep track of numbers we've seen in seen numbers set
        # Return len(nums) / 3