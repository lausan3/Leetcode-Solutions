class Solution:
    def maxDifference(self, s: str) -> int:
        letter_frequencies = [0] * 26

        for letter in s:
            i = ord('a') - ord(letter)
            letter_frequencies[i] += 1

        
        odds = list(filter(lambda x: x % 2 == 1, letter_frequencies))
        evens = list(filter(lambda y: y > 0 and y % 2 == 0, letter_frequencies))

        max_odd, max_even = max(odds), max(evens)

        if max_odd > max_even:
            return max_odd - min(evens)
        else:
            return max_even - min(odds)