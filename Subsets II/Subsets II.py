class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        curr = []

        nums.sort()

        def backtrack(i: int) -> None:
            res.append(curr.copy())

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue  # skip duplicates

                curr.append(nums[j])
                backtrack(j + 1)
                curr.pop()

        backtrack(0)

        return res
