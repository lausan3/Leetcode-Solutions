class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(max_choice_n, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return

            for i in range(max_choice_n, n + 1):
                arr.append(i)
                backtrack(i + 1, arr)
                arr.pop()

        backtrack(1, [])
        return res