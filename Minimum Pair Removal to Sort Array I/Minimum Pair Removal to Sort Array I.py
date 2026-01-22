class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        Brute Force Simulation Approach:
        1. While the array is not sorted, find the adjacent pair with the minimum sum
           and add them
        2. Count the number of operation to achieve this

        Time: O(n^2)
        Space: O(1)

        Note: We can optimize time a bit by keeping all initial sum in an array, 
        then updating the array everytime we do a simulation operation. But this i
        still O(n^2) due to needing to see if the array is sorted or not.
        """
        operation_count = 0

        for i in range(len(nums)):
            is_sorted = True

            min_sum = float('inf')
            min_indices = [0, 0]

            for j in range(1, len(nums)):
                prev, cur = nums[j - 1], nums[j]

                if prev > cur:
                    is_sorted = False

                if prev + cur < min_sum:
                    min_sum = prev + cur
                    min_indices = [j - 1, j]

            if is_sorted:
                break
            else:
                operation_count += 1

                x, y = min_indices
                nums = nums[:x] + [min_sum] + nums[y + 1:]

        return operation_count