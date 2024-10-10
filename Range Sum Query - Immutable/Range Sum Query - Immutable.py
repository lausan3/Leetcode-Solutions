class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []

        for i in range(len(nums)):
            self.prefix_sum.append(nums[i] + self.prefix_sum[i-1] if i > 0 else nums[0])
        print(self.prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 > 0:
            return self.prefix_sum[right] - self.prefix_sum[left-1]
        else: return self.prefix_sum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)