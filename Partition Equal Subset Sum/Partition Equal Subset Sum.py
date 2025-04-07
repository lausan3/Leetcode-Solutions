class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Brute force: O(n * 2^n) time (subsets). O(2^n) space
        n = len(nums)

        # Approach:
        #  Use backtracking algorithm that finds all subsets
        #    for both subsets, if their sum is equal, return true.
        #  If we can't find two equal subset sums, return false.

        def FindEqualSubsetSum(i: int, sub1: list[int], sub2: list[int]) -> bool:
            if i >= n:
                return sum(sub1) == sum(sub2)

            num = nums[i]

            # First choice: Add num to sub1
            sub1.append(num)
            found_equal_sum_1 = FindEqualSubsetSum(i + 1, sub1, sub2)
            sub1.pop()

            # Second choice: Add num to sub2
            sub2.append(num)
            found_equal_sum_2 = FindEqualSubsetSum(i + 1, sub1, sub2)
            # This needs to be here because lists in python are pass-by-ref.
            #  Omitting this .pop() will result in sub2 being ginormous.
            sub2.pop()
            
            return found_equal_sum_1 or found_equal_sum_2

        return FindEqualSubsetSum(0, [], [])