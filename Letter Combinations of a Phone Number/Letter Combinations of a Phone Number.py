class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)

        res = []
        curr = []

        def backtrack(i: int) -> None:
            if i == n:
                res.append("".join(curr))
                return

            for ltr in mapping[digits[i]]:
                curr.append(ltr)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)

        return res
