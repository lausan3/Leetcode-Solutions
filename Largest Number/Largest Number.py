class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_strings = [str(x) for x in nums]

        # print(nums_strings.sort())

        nums_strings.sort(key=lambda x: x * 10, reverse=True)

        return "".join(nums_strings)