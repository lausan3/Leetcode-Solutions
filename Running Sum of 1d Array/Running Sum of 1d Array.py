class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        running_sum = 0
        for num in nums:
            running_sum += num

            res.append(running_sum)

        return res