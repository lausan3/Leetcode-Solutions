class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search problem: 
        
        # # edge case: only two numbers, return minimum
        # if len(nums) == 2:
        #     return min(nums[0], nums[1])

        # l, r = 0, len(nums) - 1

        # while l < r:
        #     m = (l + r) // 2
        #     left, right, mid = nums[l], nums[r], nums[m]
            
        #     print(f"searching limits: ({l, left}, {r, right}, {m, mid})")

        #     # idea: compare middle element with left and right element to see which one is smallest, then adjust to
        #     # search that side of the array
        #     ## left is smaller than right, search left
        #     if left < right:
        #         r = m - 1
        #         print(f"left search, new limits: ({l, nums[l]}, {r, nums[r]})")
        #     ## right is smaller than left, search right
        #     elif right < left:
        #         l = m + 1
        #         print(f"right search, new limits: ({l, nums[l]}, {r, nums[r]})")

        # idea: there is always a left sorted portion that is greater than every # in the right sorted portion because of
        # how the rotation works. Therefore, if the number at the midpoint is less than the number at the left, then that
        # means that we're in the right sorted portion, so we keep searching there since it's going to be smallest.
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
                
        return res