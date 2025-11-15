class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (len(nums))

        for i in range(n):
            ans[i * 2] = nums[i]
            ans[i * 2 + 1] = nums[i + n]

        return ans
