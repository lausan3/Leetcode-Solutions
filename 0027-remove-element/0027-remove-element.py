class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        r = len(nums) - 1

        for i, num in enumerate(nums):
            # print(f"current index: {i}. current num: {num}. current nums: {nums}")
            if num == val:
                while r > i and nums[r] == val:
                    r -= 1

                temp = nums[r]
                nums[r] = nums[i]
                nums[i] = temp

            # print(f"k: {k}. new num: {nums}")

        for i in range(len(nums)):
            if nums[i] != val:
                k+=1

        return k