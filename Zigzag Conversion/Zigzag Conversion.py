class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Brute Force 2D Array Solution:
        1. Represent the string in a stack
        2. Create a 2D array to represent the zigzag of size numRows * len(s)
        3. Until the stack is empty, repeat this pattern:
           3a. Place numRows letters downwards
           3b. Go up and right one and place another letter
           3c. Repeat this numRows - 2 times
           3d. Repeat from 3a
        4. Return the resulting row-by-row string representation of the array.

        Time: O(numRows * n)
        Space: O(numRows * n)
        """
        n = len(s)
        letters = list(s)[::-1]
        zigzag = [ [None for _ in range(n)] for _ in range(numRows) ]
        r = c = 0
        down_row_index = max(1, numRows - 1)

        while letters:
            letter = letters.pop()

            zigzag[r][c] = letter

            # down
            if c % down_row_index == 0 and r < numRows - 1:
                r += 1
            # diagonal
            else:
                c += 1
                r -= 1

        res = ""

        for r in range(numRows):
            for c in range(n):
                if zigzag[r][c]:
                    res += zigzag[r][c]

        return res