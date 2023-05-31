class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occuranceDict = {}
        targetn = len(nums) / 2

        for num in nums:
            # if not in dictionary, add it
            if num not in occuranceDict:
                occuranceDict[num] = 1
            else:
                occuranceDict[num] += 1

        # check for occurance greater than targetn
        for key in occuranceDict:
            if occuranceDict[key] > targetn:
                return key

        return -1