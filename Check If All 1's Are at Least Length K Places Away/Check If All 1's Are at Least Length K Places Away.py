class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l = r = 0

        while l < n and r < n:
            while l < n and nums[l] != 1:
                l += 1
            
            r = l + 1

            while r < n and nums[r] != 1:
                r += 1
            
            if l < n and r < n and nums[l] == 1 and nums[r] == 1:
                if r - l - 1 < k:
                    return False
                else:
                    l = r

        return True