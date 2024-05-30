class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # O(n) where n is the length of the larger string
        
        res = []
        oneLength, twoLength = len(word1), len(word2)

        for i in range(max(oneLength, twoLength)):
            if i < oneLength:
                res.append(word1[i])
            if i < twoLength:
                res.append(word2[i])

        return "".join(res)