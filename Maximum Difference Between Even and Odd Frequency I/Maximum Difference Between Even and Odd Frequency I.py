class Solution:
    def maxDifference(self, s: str) -> int:
        letter_frequencies = [0] * 26

        for letter in s:
            i = ord('a') - ord(letter)
            letter_frequencies[i] += 1

        
        odds = filter(lambda x: x > 0 and x % 2 == 1, letter_frequencies)
        evens = filter(lambda y: y > 0 and y % 2 == 0, letter_frequencies)

        return abs(max(odds) - min(evens))