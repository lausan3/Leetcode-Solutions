class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## Big Idea: an important fact about sorted arrays is that all duplicate numbers will be placed next to each other.
        ## Using this fact, we can ignore them and check for non-duplicates, moving them by the amount of duplicates we
        ## encounter.
        k = 0

        for index in range(len(nums)):
            # print(f"PASS {index}:")
            if index < len(nums) - 1 and nums[index] == nums[index + 1]:
                # print(f"Found duplicate, continuing")
                continue
            
            ## Update array in place by "adding" a new unique number to the imaginary unique nubmers array using k and the
            ## index of the unique number.
            nums[k] = nums[index]
            k += 1
            # print(f"Unique number found: {nums[index]}, swapping {nums[k]} and {nums[index]}. New k: {k}")
            # print(f"New array: {nums}")

        return k