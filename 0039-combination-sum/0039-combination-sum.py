class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            # candidates cannot be negative, end recursion early if we find the target
            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
                return

            # cannot add any more candidates, end recursion
            if sum(subset) > target or i >= len(candidates):
                return
            
            # add this index to subset
            subset.append(candidates[i])
            dfs(i)

            subset.pop()

            # add next number to subset
            subset.append(candidates[i])
            dfs(i + 1)

            subset.pop()

            # skip this number
            dfs(i + 1)

        dfs(0)

        return res