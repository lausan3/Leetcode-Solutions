class Solution:
    def possibleStringCount(self, word: str) -> int:
        # approach:
        # init variable for total count of possible words including itself
        # for each letter in word,
        #   if next letter is the same as the current letter,
        #       add one to count
        # return count

        total_ways = 1

        # O(n)
        for r in range(1, len(word)):
            if word[r] == word[r - 1]:
                total_ways += 1
        
        return total_ways