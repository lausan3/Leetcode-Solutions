class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        This is a standard backtracking problem, but with a lot more cases to consider.

        We backtrack for the following cases:
            1. character is not valid, consider the character in ending string
            2. character is valid, but we skip it
            3. character is "(", consider it
            4. character is ")" and is matched, consider it

         where valid means "(" or ")"

        Then, whenever we reach the end of the string, we compare the amount of removals (characters we skip)
         to the minimum we've seen, adding it to the result only if it's <= to the minimum.

        Time: O(2^n)
        Space: O(n) since we are only considering recursive call stack memory usage up to the end of the string.
        """
        n = len(s)
        valid = set()
        min_rem = n

        def backtrack(i: int, curr: List[str], left_count: int, right_count: int, removal_count: int):
            if i >= n:
                nonlocal min_rem
                nonlocal valid

                if left_count == right_count and removal_count <= min_rem:
                    if removal_count < min_rem:
                        min_rem = removal_count
                        valid = set()

                    valid.add("".join(curr))

                return 
            
            char = s[i]

            if char != "(" and char != ")":
                curr.append(char)
                backtrack(i + 1, curr, left_count, right_count, removal_count) # add current non parentheses char

                curr.pop()
            else:
                backtrack(i + 1, curr, left_count, right_count, removal_count + 1) # skip current parentheses

                curr.append(char)

                if char == "(": # "(" must be added
                    backtrack(i + 1, curr, left_count + 1, right_count, removal_count)
                elif right_count < left_count: # char is ")" and matched.
                    backtrack(i + 1, curr, left_count, right_count + 1, removal_count)
                
                curr.pop()

        backtrack(0, [], 0, 0, 0)

        return list(valid)