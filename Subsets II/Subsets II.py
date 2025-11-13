class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        curr = []

        nums.sort()

        def backtrack(i: int) -> None:
            if i == n:
                if curr not in res:
                    res.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i + 1)

            curr.pop()
            backtrack(i + 1)

        backtrack(0)

        return res
