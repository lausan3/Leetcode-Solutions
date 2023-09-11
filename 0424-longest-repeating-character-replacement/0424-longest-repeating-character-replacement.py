class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window problem: to solve this, we keep a count of the letters in our sliding window and see if our
        # window is valid (size of window - highest occuring letter = amount of letters we can change to create
        # a longer substring <= k value = valid). if it's valid, we grow our window, keeping track of the max length as
        # we go. if invalid, we shrink the window.
        maxC = 0 # max count of letters at the moment. we do this to lower the time complexity from O(26 * n) to O(n) 
                 # because we don't have to search through the possible 26-alphabetically long dictionary count
        
        count = {}
        currMax = 0
        l = 0

        # iterate through string
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # check if character we just added is new max character count
            maxC = max(maxC, count[s[r]])
            
            # valid substring?
            while (r - l + 1) - maxC > k:
                count[s[l]] -= 1
                l += 1
            
            currMax = max(currMax, r - l + 1)

        return currMax