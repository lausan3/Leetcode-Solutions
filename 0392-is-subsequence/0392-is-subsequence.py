class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # O(n + m) where n = len(t) and m = len(s)
        letters = [char for char in s[::-1]]

        for letter in t:
            if len(letters) == 0:
                return True
            
            if letter == letters[-1]:
                popped = letters.pop()

        
        return len(letters) == 0