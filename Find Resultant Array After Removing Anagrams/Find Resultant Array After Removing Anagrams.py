class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # There's the obvious O(n^2) time, O(1) space brute-force solution, and this
        # O(n) time O(26n) space solution by preprocessing all words for counts
        
        unique_counters = {}

        # get letter counts and track them in unique counters
        # O(n) or O(n^2)?
        for word in words:
            if word in unique_counters:
                continue

            count = ["0"] * 26

            for letter in word:
                i = ord(letter) - ord('a')
                # using strings here to avoid a list comprehension turning all 
                # nums to strings
                count[i] = str(int(count[i]) + 1)

            encoded = ".".join(count)
            unique_counters[word] = encoded

        # compare words
        result = [words[0]]

        for i in range(1, len(words)):
            prev, curr = words[i-1], words[i]

            isAnagram = unique_counters[prev] == unique_counters[curr]
            if not isAnagram:
                result.append(curr)

        return result