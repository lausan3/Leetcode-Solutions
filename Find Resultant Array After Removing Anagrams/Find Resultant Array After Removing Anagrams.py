class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # There's the obvious O(n^2) time, O(1) space brute-force solution, and this
        # O(n) time O(26n) space solution by preprocessing all words for counts
        
        unique_counters = set()
        result = []

        # get letter counts and track them in unique counters
        # O(n) or O(n^2)?
        for word in words:
            count = ["0"] * 26

            for letter in word:
                i = ord('a') - ord(letter) - 1
                # using strings here to avoid a list comprehension turning all 
                # nums to strings
                count[i] = str(int(count[i]) + 1)

            encoded = ".".join(count)
            
            # if encoded count is already in the set, we don't want it in the output
            if encoded not in unique_counters:
                unique_counters.add(encoded)
                result.append(word)

        return result