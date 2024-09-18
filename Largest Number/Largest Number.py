class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_strings = [str(x) for x in nums]

        nums_strings.sort(key=lambda x: x * 10, reverse=True)

        if nums_strings[0] == "0": return "0"

        return "".join(nums_strings)