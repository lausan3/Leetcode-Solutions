class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        # solution: for every value in nums, get the product of all the values before it (prefix) 
        # and storing them in the position in the output array that it's before, and then multiply them
        # by the postfix product.

        # prefix solving
        prefix = 1
        for i in range(len(nums)):
            answer.append(prefix)

            prefix *= nums[i]

        # postfix solving - same thing but in reverse
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix

            postfix *= nums[i]
    
        return answer