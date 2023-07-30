class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict = {}

        for i in range(len(s)):
            # loop through both words and count how many letters are in each word
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in dict:
                return False
            elif dict[t[i]] >= 1:
                dict[t[i]] -= 1
            else: return False

        return True