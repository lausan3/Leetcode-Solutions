class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = maxVowels = currVowels = 0
        vowels = "aeiou"
        lastWasVowel = False

        for i in range(k):
            char = s[:k][i]

            if char in vowels:
                currVowels += 1

        if s[k - 1] in vowels: lastWasVowel = True
        maxVowels = max(maxVowels, currVowels)

        for r in range(k - 1, len(s)):
            if lastWasVowel: currVowels -= 1
            if s[r] in vowels: 
                currVowels += 1
            
            if s[l] in vowels: lastWasVowel = True
            else: lastWasVowel = False

            maxVowels = max(maxVowels, currVowels)

            l += 1

        return maxVowels