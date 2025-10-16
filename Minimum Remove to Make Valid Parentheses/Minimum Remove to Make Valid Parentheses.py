class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # O(n) time, O(n) space where n = len(s)
        # this problem is a trick. the minimum number of parentheses removed
        #  is just the correct string with parentheses matched.
        chars = [x for x in s]
        parens = []

        for i, char in enumerate(chars):
            if (char == "(" or 
               (char == ")" and (not parens or (parens and parens[-1][1] != "(")))
            ):
                parens.append((i, char))
            elif char == ")" and parens and parens[-1][1] == "(":
                parens.pop()

        for i, _ in parens:
            chars[i] = ""

        return "".join(chars)

            
            

        
        