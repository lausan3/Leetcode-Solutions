class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]
            
        for i in range(len(nums)):     
            num = nums.pop(0)            # pop bottom element
            perms = self.permute(nums)   # get top element [1], [2], [3]

            for perm in perms:
                perm.append(num)         # append popped num

            res.extend(perms)            # append all perms into res
            nums.append(num)

        return res