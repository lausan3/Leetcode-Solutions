class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [nums[i] + nums[i-1] if i > 0 else nums[0] for i in range(1, len(nums))]
        print(self.prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        pass


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)