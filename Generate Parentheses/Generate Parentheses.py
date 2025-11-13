class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr: list[str], opened: int, closed: int):
            if opened == closed == n:
                res.append("".join(curr))
                return

            # decisions are to append an open paren or closed paren
            if opened < n:
                curr.append("(")
                backtrack(curr, opened + 1, closed)
                curr.pop()

            if opened > closed and closed < n:
                curr.append(")")
                backtrack(curr, opened, closed + 1)
                curr.pop()

        backtrack([], 0, 0)

        return res
